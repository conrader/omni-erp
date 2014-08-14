from django.contrib import admin
from django.contrib.auth.models import * 
from django.db.models import Count
from django.contrib.admin.views.main import ChangeList
from django.db.models import Sum, Avg

from crm.models import Company, Person, Order, Commission, Contact, Suborder
from config.models import ContactWay, Source, Industry, Product, CommissionRate, LeadStatus, Province, DeviceStatus, Country
from devices.models import Device


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name','industry','source','served_by','people_count','order_count')
    list_filter = ['industry','source','served_by','province']
    #change_list_filter_template = "admin/filter_listing.html"
    fieldsets = [
        ('Company details',{'fields': ['name','adress',('country','province')]}),
        ('Additional information',{'fields': [('industry','source','served_by')]}),
	]

    def queryset(self, request):
        return Company.objects.annotate(show_person_count=Count('person'), show_order_count=Count('order'))

    def people_count(self, inst):
        return inst.show_person_count

    def order_count(self, inst):
        return inst.show_order_count
    
    people_count.short_description = 'Number of People'
    order_count.short_description = "Number of Orders"

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name','company','tel','email',)
    list_filter = ('company',)
    fieldsets = [
        ('Person details',{'fields': ['name','company',('tel','email')]}),
    ]
    
    raw_id_fields = ('company',)
    autocomplete_lookup_fields = {
    'fk': ['company'],
    }

class SuborderInline(admin.TabularInline):
    model = Suborder
    extra = 1

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id','value','company','person','status','proforma','invoice','paid','user')
    list_filter = ['company','user','person','proforma','invoice','value','paid']
    fieldsets = [
        ('Basic details',{'fields': [('company','person','user')]}),
        ('Additional information',{'fields': [('value','status'),('proforma','invoice','paid')]}),
        ]

    inlines = [SuborderInline]

    def get_changelist(self, request, **kwargs):
        """Override the default changelist"""
        return OrderItemChangeList

    raw_id_fields = ('company','person',)
    autocomplete_lookup_fields = {
    'fk': ['company','person'],
    }

class ContactAdmin(admin.ModelAdmin):
    list_display = ('time','person','show_company','user','way',)
    list_filter = ('user',)
    fieldsets = [
        ('Contact details',{'fields': ['time','person','info',('way','user')]}),
    ]
    
    raw_id_fields = ('person',)
    autocomplete_lookup_fields = {
    'fk': ['person'],
    }

    def show_company(self, inst):
        return inst.person.company

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('serial','client','model','status',)
    list_filter = ('model','status',)
    fieldsets = [
        ('Device details',{'fields': ['serial','client',('model','status'),]}),
    ]
    
    raw_id_fields = ('client',)
    autocomplete_lookup_fields = {
    'fk': ['client'],
    }

class OrderItemChangeList(ChangeList):
    """Custom total rows at bottom of changlist"""

    def get_total_value(self, queryset):
        total = Order()
        total.order_id = "Total value"
        total.proforma = ""
        total.invoice = ""
        total.paid = None
        total_dict = queryset.aggregate(Sum('value'))
        setattr(total, 'value', total_dict.items()[0][1])
        return total

    def get_average_value(self, queryset):
        avg = Order()
        avg.order_id = "Average value"
        avg.proforma = ""
        avg.invoice = ""
        avg.paid = None
        avg_dict = queryset.aggregate(Avg('value'))
        setattr(avg, 'value', avg_dict.items()[0][1])
        return avg

    def get_results(self, request):
        super(OrderItemChangeList, self).get_results(request)
        total_value = self.get_total_value(self.query_set)
        average_value = self.get_average_value(self.query_set)
        # HACK: in order to get the objects loaded we need to call for
        # queryset results once so simple len function does it
        len(self.result_list)
        self.result_list._result_cache.append(total_value)
        self.result_list._result_cache.append(average_value)


admin.site.register(Company, CompanyAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.register(Country)
admin.site.register(ContactWay)
admin.site.register(Source)
admin.site.register(Industry)
admin.site.register(Product)
admin.site.register(CommissionRate)
admin.site.register(LeadStatus)
admin.site.register(Province)
admin.site.register(DeviceStatus)

admin.site.register(Device, DeviceAdmin)


#admin.site.unregister(User)
#admin.site.unregister(Group)


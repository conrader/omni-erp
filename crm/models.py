from django.db import models
from datetime import datetime    
from django.contrib import admin
import config
import devices
from django.contrib.auth.models import User

def user_unicode_patch(self):
	if self.first_name == '' or self.last_name == '':
		return unicode(self.username)
	else:	
		return unicode('%s %s' % (self.first_name, self.last_name))

User.__unicode__ = user_unicode_patch

class Contact(models.Model):
	time = models.DateTimeField(default=datetime.now, blank=True)
	user = models.ForeignKey(User,related_name='contact_made_by')
	person = models.ForeignKey('Person')
	info = models.TextField(max_length=500, null=True, blank=True)
	way = models.ForeignKey('config.ContactWay', null=True, blank=True)

	def __unicode__(self):
		return unicode('%s %s' % (str(self.time)[:-9], self.person.company))

	class Meta:
		app_label = 'crm'

class Company(models.Model):
	name = models.CharField(max_length=30)
	adress = models.TextField(max_length=200)
	country =  models.ForeignKey('config.Country')
	province = models.ForeignKey('config.Province',null=True, blank=True)
	industry = models.ForeignKey('config.Industry')
	source = models.ForeignKey('config.Source')
	served_by = models.ForeignKey(User, null=True, blank=True)
	
	def __unicode__(self):
		return unicode(self.name)

	def related_label(self):
		return self.name


	class Meta:
		verbose_name_plural = "companies"
        app_label = 'crm'

class Person(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=30)
	tel = models.CharField(max_length=30)
	company = models.ForeignKey('Company')

	def __unicode__(self):
		return unicode(self.name)

	def related_label(self):
		return self.name

	class Meta:
		verbose_name_plural = "people"
        app_label = 'crm'


class Order(models.Model):
	order_id = models.AutoField(primary_key=True,editable=True)
	user = models.ForeignKey(User,related_name='order_made_by',blank=True,null=True)
	company = models.ForeignKey('Company')
	person = models.ForeignKey('Person')
	value = models.IntegerField()
	status = models.ForeignKey('config.LeadStatus')
	proforma = models.DateField(verbose_name="Proforma Invoice",blank=True,null=True)
	invoice = models.DateField(verbose_name="VAT Invoice",blank=True,null=True)
	paid = models.BooleanField()

	def __unicode__(self):
		return unicode(str(self.order_id))

	class Meta:
		app_label = 'crm'

	@property
	def id(self):
		return self.order_id

class Commission(models.Model):
	user = models.ForeignKey(User,related_name='commission_made_by')
	order = models.ForeignKey('Order')
	rate = models.ForeignKey('config.CommissionRate')

	def __unicode__(self):
		return unicode(self.order)

	class Meta:
		app_label = 'crm'

class Suborder(models.Model):
	product = models.ForeignKey('config.Product')
	quantity = models.IntegerField()
	order = models.ForeignKey(Order)

	class Meta:
		app_label = 'crm'


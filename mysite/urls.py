from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    (r'^admin/',  include(admin.site.urls)), # admin site
    (r'^/',  include(admin.site.urls)), # admin site
#    url(r'^admin/', include(admin.site.urls)),
)


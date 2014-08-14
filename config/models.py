from django.db import models
from django.contrib.auth.models import User
#from crm.models import *

"""
class Employee(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = 'config'
"""

class ContactWay(models.Model):
	way = models.CharField(max_length=30)

	def __unicode__(self):
		return unicode(self.way)
	
	class Meta:
		app_label = 'config'

class Source(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = 'config'

class Industry(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return unicode(self.name)
	
	class Meta:
		verbose_name_plural = "industries"
		app_label = 'config'

class Product(models.Model):
	name = models.CharField(max_length=30)
	price = models.IntegerField()

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = 'config'

class CommissionRate(models.Model):
	name = models.CharField(max_length=30)
	product = models.ForeignKey(Product)
	rate = models.IntegerField()

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name_plural = "Commision Rates"
		verbose_name = "Commission Rate"
		app_label = 'config'

class LeadStatus(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name_plural = "Lead Statuses"
		verbose_name = "Lead Status"
		app_label = 'config'

class Province(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = 'config'

class Country(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		app_label = 'config'
		verbose_name_plural = "Countries"

class DeviceStatus(models.Model):
	name = models.CharField(max_length=30)

	def __unicode__(self):
		return unicode(self.name)

	class Meta:
		verbose_name_plural = "Device Statuses"
		verbose_name = "Device Status"
		app_label = 'config'


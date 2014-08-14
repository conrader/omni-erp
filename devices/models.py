from django.db import models
from datetime import datetime    
from django.contrib import admin
import config
import crm
from django.contrib.auth.models import User

class Device(models.Model):
	serial = models.CharField(max_length=20)
	model = models.ForeignKey('config.Product')
	client = models.ForeignKey('crm.Company',blank=True,null=True)
	status = models.ForeignKey('config.DeviceStatus',blank=True,null=True)
	qc_made =  models.ForeignKey(User,blank=True,null=True)
	qc_time = models.DateField(blank=True,null=True)

	def __unicode__(self):
		return unicode(self.serial)

	class Meta:
		app_label = 'devices'

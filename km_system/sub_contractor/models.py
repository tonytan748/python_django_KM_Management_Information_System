from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from supplier.models import Supplier

class Modelify(models.Model):
	create_by=models.CharField(max_length=120)
	create_date=models.DateTimeField(auto_now_add=True)
	edit_by=models.CharField(max_length=120,blank=True,null=True)
	edit_date=models.DateTimeField(auto_now=True)

class Subcon(Modelify):
	code=models.CharField(max_length=10,blank=False,null=False,unique=True)
	name=models.CharField(max_length=250,blank=False,null=False,unique=True)
	tel=models.CharField(max_length=50,blank=True,null=True)
	fax=models.CharField(max_length=50,blank=True,null=True)
	contact=models.CharField(max_length=100,blank=True,null=True)
	address=models.TextField(blank=True,null=True)
	scope_of_work=models.CharField(max_length=200,blank=True,null=True)
	gst_verification=models.BooleanField(default=True)
	gst_reg_no=models.CharField(max_length=200,blank=True,null=True)
	remark=models.TextField(blank=True,null=True)
	
	def __unicode__(self):
		return self.name
	class Meta:
		ordering=['code','name']

	def get_absolute_url(self):
		return reverse('subcon',kwargs={'pk':self.id})



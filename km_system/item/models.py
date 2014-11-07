from django.db import models
from django.core.urlresolvers import reverse

from django.contrib.auth.models import User
from supplier.models import Supplier

class Modelify(models.Model):
	create_by=models.CharField(max_length=120)
	create_date=models.DateTimeField(auto_now_add=True)
	edit_by=models.CharField(max_length=120,blank=True,null=True)
	edit_date=models.DateTimeField(auto_now=True)

class Kinds(Modelify):
	main_category=models.CharField(max_length=200)
	sub_category=models.CharField(max_length=200)

	def __unicode__(self):
		return "%s-%s" % (self.main_category,self.sub_category)
	class META:
		ordering=['main_category',]

class Item(Modelify):
	code=models.CharField(max_length=10,blank=False,null=False)
	name=models.TextField(blank=False,null=False)
	supplier=models.ForeignKey(Supplier)
	category=models.ForeignKey(Kinds)
	large_uom=models.CharField(max_length=10)
	large_qty=models.IntegerField()
	large_price=models.FloatField()
	med_uom=models.CharField(max_length=10,blank=True,null=True)
	med_qty=models.IntegerField(blank=True,null=True)
	med_price=models.FloatField(blank=True,null=True)
	sml_uom=models.CharField(max_length=10)
	sml_qty=models.IntegerField()
	sml_price=models.FloatField()
	remark=models.TextField(blank=True,null=True)
	
	def __unicode__(self):
		return self.name
	class Meta:
		ordering=['category','supplier','name']

	def get_absolute_url(self):
		return reverse('list',kwargs={'pk':self.id})



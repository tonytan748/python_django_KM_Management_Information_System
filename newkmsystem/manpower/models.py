from django.db import models
from django.contrib.auth.models import User
import datetime

from django.utils.timezone import get_current_timezone
tz = get_current_timezone()
fmt="%Y-%m-%d %H:%M:%S.%f"

class Shift(models.Model):
	name=models.CharField(max_length=100,unique=True)
	def __unicode__(self):
		return self.name
	class Meta:
		ordering=['name',]

class Employee(models.Model):
	code=models.CharField(max_length=10,unique=True)
	name=models.CharField(max_length=150,unique=True)

	def __unicode__(self):
		return self.code

	class Meta:
		ordering=['code',]

class Project(models.Model):
	code=models.CharField(max_length=5)
	code_word=models.CharField(max_length=1)
	rev=models.IntegerField(default=0)
	name_1=models.CharField(max_length=150,blank=True)
	name_2=models.CharField(max_length=300,blank=True)
	payment=models.CharField(max_length=50,blank=True)
	status=models.CharField(max_length=50)

	def __unicode__(self):
		if self.rev==0:
			prev=""
		else:
			prev=" - "+str(self.rev+100)[1:]
		return "%s %s%s"%(self.code,self.code_word,prev)

	class Meta:
		ordering=['code']

class Salary(models.Model):
	employee=models.ForeignKey(Employee,unique=True)
	daily=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	ot125=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	ot150=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	ot200=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	morning=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	everyday=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	shift=models.CharField(max_length=50)
	create_by=models.CharField(max_length=120)
	create_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.employee

	class Meta:
		ordering=['employee']

class ManPower(models.Model):
	employee=models.ForeignKey(Employee)
	project=models.ForeignKey(Project)
	time_in=models.CharField(max_length=30)
	time_out=models.CharField(max_length=30)
	lunch=models.IntegerField(default=1)
	shift=models.ForeignKey(Shift)
	working_time=models.CharField(max_length=120)
	remark=models.TextField()
	create_by=models.CharField(max_length=120)
	create_date=models.DateTimeField(auto_now_add=True)

	is_checked=models.BooleanField(default=False)
	checked_by=models.CharField(max_length=200,blank=True,null=True)
	checked_date=models.DateTimeField(auto_now_add=True)

	time100=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	time100salary=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	time125=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	time125salary=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	time150=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	time150salary=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	time200=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	time200salary=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	timeremark=models.TextField()

	is_payed=models.BooleanField(default=False)
	payed_period=models.CharField(max_length=50,blank=True,null=True)

	def __unicode__(self):
		return self.time_in

	class Meta:
		ordering=['time_in']

#	def save(self,*args,**kwargs):
#		self.working_time=datetime.datetime.strftime((datetime.datetime.strptime(self.time_out,fmt)-datetime.datetime.striptime(self.time_in,fmt),fmt)
#		super(ManPower,self).save(*args,**kwargs)

class Lend(models.Model):
	employee=models.ForeignKey(Employee)
	payed_period=models.CharField(max_length=50,blank=True,null=True)
	lend_desc=models.TextField()
	lend_acount=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	additional_desc=models.TextField()
	additional_acount=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	create_by=models.ForeignKey(User)
	create_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.lend_desc

	class Meta:
		ordering=['-create_date']

	



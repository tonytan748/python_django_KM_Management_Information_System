from django.db import models
from django.contrib.auth.models import User
import datetime

class Modify(models.Model):
	create_by=models.CharField(max_length=120)
	create_date=models.DateTimeField(auto_now_add=True)

class Employee(models.Model):
	code=models.CharField(max_length=10,unique=True)
	name=models.CharField(max_length=150,unique=True)

	def __unicode__(self):
		return self.code

	class Meta:
		ordering=['code',]

class Project(models.Model):
	code=models.CharField(max_length=5,unique=True)
	code_1=models.CharField(max_length=1)
	rev=models.IntegerField(default=0)
	name_1=models.CharField(max_length=150,blank=True)
	name_2=models.CharField(max_length=300,blank=True)
	payment=models.CharField(max_length=50,blank=True)
	status=modles.CharField(max_length=50)
	
	def __unicode__(self):
		return "%s %s - %s"%(self.code,self.code_1,str(self.rev+100)[1:])

	class Meta:
		ordering=['code']

class Salary(Modify):
	employee=models.ForeignKey(Employee)
	daily=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	ot1_25=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	ot1_50=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	ot2_00=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	morning=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	everyday=models.DecimalField(max_digits=16,decimal_places=3,default=0)
	shift=models.CharField(max_length=50)

	def __unicode__(self):
		return self.employee

	class Meta:
		ordering=['employee']

class ManPower(Modify):
	employee=models.ForeignKey(Employee)
	project=models.ForeignKey(Project)
	time_in=models.DateTimeField()
	time_out=models.DateTimeField()
	lunch=models.IntegerField(default=1)
	shift=models.CharField(max_length=2)
	working_time=models.DecimalField(max_length=16,decimal_places=3,default=0)
	remark=models.TextField()
	is_checked=models.BooleanField(default=False)
	checked_by=models.CharField(max_length=200,blank=True,null=True)
	checked_date=models.DateTimeField(auto_now_add=True)

	time100=models.DecimalField(max_length=16,decimal_places=3,default=0)
	time100salary=models.DecimalField(max_length=16,decimal_places=3,default=0)
	time125=models.DecimalField(max_length=16,decimal_places=3,default=0)
	time125salary=models.DecimalField(max_length=16,decimal_places=3,default=0)
	time150=models.DecimalField(max_length=16,decimal_places=3,default=0)
	time150salary=models.DecimalField(max_length=16,decimal_places=3,default=0)
	time200=models.DecimalField(max_length=16,decimal_places=3,default=0)
	time200salary=models.DecimalField(max_length=16,decimal_places=3,default=0)
	timeremark=models.TextField()

	is_payed=models.BooleanField(defautl=False)
	payed_period=models.CharField(max_langth=50,blank=True,null=True)
	
	def __unicode__(self):
		return self.time_in

	class Meta:
		ordering=['time_in']

	def save(self,*args,**kwargs):
		self.working_time=datetime.timedelta(self.time_out-self.time_in)
		super(ManPower,self).save(*args,**kwargs)

def EmployeeSalary(models.Model):
	pass

class Lend(models.Model):
	employee=models.Foreignkey(Employee)
	payed_period=models.CharField(max_length=50,blank=True,null=True)
	lend_desc=models.TextField()
	lend_acount=models.DecimalField(max_length=16,decimal_places=3,default=0)
	additional_desc=models.TextFild()
	additional_acount=models.DecimalField(max_length=16,decimal_places=3,default=0)
	create_by=models.ForeignKey(User)
	create_date=models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.lend_desc

	class Meta:
		ordering=['-create_date']

	



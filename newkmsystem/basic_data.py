import datetime
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','newkmsystem.settings')
 
import django
django.setup()
 
from manpower.models import Employee,Project,Salary,ManPower,Lend,Shift
 
def add_shift(name):
	p=Shift.objects.get_or_create(name=name)[0]
	return p
def add_employee(code,name):
	c=Employee.objects.get_or_create(code=code,name=name)[0]
	return c
def add_project(code,code_word,rev,name_1,name_2,payment,status):
	c=Project.objects.get_or_create(code=code,code_word=code_word,rev=rev,name_1=name_1,name_2=name_2,payment=payment,status=status)[0]
	return c
def add_salary(employee,daily,ot125,ot150,ot200,morning,everyday,shift,create_by,create_date):
	c=Salary.objects.get_or_create(employee=employee,daily=daily,ot125=ot125,ot150=ot150,ot200=ot200,morning=morning,everyday=everyday,shift=shift,create_by=create_by,create_date=create_date)[0]
	return c
def add_lend(employee,payed_period,lend_desc,lend_account,additional_desc,additional_acount,create_by,create_date):
	c=Lend.objects.get_or_create(employee=employee,payed_period=payed_period,lend_desc=lend_desc,lend_account=lend_account,additional_desc=additional_desc,additional_acount=additional_acount,create_by=create_by,create_date=create_date)[0]
	return c
def add_manpower(employee,project,time_in,time_out,lunch,shift,working_time,remark,create_by):
	c=ManPower.objects.get_or_create(employee=employee,project=project,time_in=time_in,time_out=time_out,lunch=lunch,shift=shift,working_time=working_time,remark=remark,create_by=create_by)[0]
	return c

def populate():
	add_one_shift=add_shift(name="D1")
	add_one_project=add_project(code="12345",code_word="W",rev=0,name_1="abc",name_2="ddddddd.ddd",payment="PROCESS",status="ON GOING")
	add_one_employee=add_employee(code="BA00122",name="Nmsfsfk dfsldf fdkd")
	add_two_employee=add_employee(code="CC00023",name="Tondfha fjjuH hdf")
	
	add_manpower(employee=add_one_employee,project=add_one_project,time_in=datetime.datetime.now()-datetime.timedelta(hours=8),time_out=datetime.datetime.now(),lunch=1,shift=add_one_shift,working_time=datetime.timedelta(hours=8),remark="Remark 1...",create_by="tonytan")
	add_manpower(employee=add_two_employee,project=add_one_project,time_in=datetime.datetime.now()-datetime.timedelta(hours=7),time_out=datetime.datetime.now(),lunch=1,shift=add_one_shift,working_time=datetime.timedelta(hours=7),remark="Remark 2...",create_by="tonytan")

if __name__=='__main__':
	print "String Rango population script.."
	populate()
from models import *

import datetime

fmt="%Y-%m-%d %H:%M:%S.%f"

def add_new_shift(name):
	if name:
		s=Shift.objects.create(name=name)
		s.save()
		return True
	return False

def add_new_employee(code=None,name=None):
	e=Employee.objects.create(code=code,name=name)
	e.save()
	
def add_new_project(code,code_word,rev,name_1,name_2,payment,status):
	p=Project.objects.create(code=code,code_word=code_word,rev=rev,name_1=name_1,name_2=name_2,payment=payment,status=status)
	p.save()
	
def add_new_manpower(employee_id=None,project_id=None,time_in=None,time_out=None,lunch=None,shift_id=None,working_time=None,remark=None,create_by=None):
	e=Emloyee.objects.get(id=employee_id)
	p=Project.objects.get(id=project_id)
	s=Shift.objects.get(id=shift_id)
	m=ManPower.objects.create(employee=e,project=p,time_in=time_in,time_out=time_out,lunch=lunch,shift=s,working_time=working_time,remark=remark,create_by=create_by,create_date=create_date)
	
if __name__=="__main__":
	add_new_shift(name="D2")
	add_new_shift(name="D3")
	add_new_shift(name="N1")
	add_new_shift(name="N2")
	
	add_new_employee(code="OS00218",name="TONY TAN")
	add_new_employee(code="BI00018",name="TON")
	add_new_employee(code="BA00042",name="MOAN")
	
	add_new_project(code="14037",code_word="Q",rev=0,name_1="RESIDENTIAL -  SEMI DETACHED HOUSE",name_2="5A QUEENS ROAD LV 1 SINGAPORE 266783",payment="",status="ON GOING")
	add_new_project(code="12762",code_word="P",rev=3,name_1="3 STOREY TERRACE HOUSE",name_2="31 PEBBLE LANE SINGAPORE 437580",payment="",status="ON GOING")
	add_new_project(code="14859",code_word="T",rev=0,name_1="PCS SECURITY PTE LTD (T9 -  PHASE 3)",name_2="NO 9 TAMPINES STREET 92 SINGAPORE 528871",payment="",status="ON GOING")
	
	add_new_manpower(employee_id=1,project_id=1,time_in=datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(hours=3),fmt),time_out=datetime.datetime.strftime(datetime.datetime.now(),fmt),lunch=1,shift_id=1,remark="remark 01",create_by="tonytan")
	add_new_manpower(employee_id=2,project_id=2,time_in=datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(hours=3),fmt),time_out=datetime.datetime.strftime(datetime.datetime.now(),fmt),lunch=1,shift_id=2,remark="remark 02",create_by="tonytan")
	add_new_manpower(employee_id=1,project_id=1,time_in=datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(hours=3),fmt),time_out=datetime.datetime.strftime(datetime.datetime.now(),fmt),lunch=1,shift_id=1,remark="remark 03",create_by="tonytan")
	add_new_manpower(employee_id=1,project_id=1,time_in=datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(hours=3),fmt),time_out=datetime.datetime.strftime(datetime.datetime.now(),fmt),lunch=1,shift_id=1,remark="remark 04",create_by="tonytan")
	add_new_manpower(employee_id=1,project_id=1,time_in=datetime.datetime.strftime(datetime.datetime.now()-datetime.timedelta(hours=3),fmt),time_out=datetime.datetime.strftime(datetime.datetime.now(),fmt),lunch=1,shift_id=1,remark="remark 05",create_by="tonytan")
	
	
	
	
	
	
	
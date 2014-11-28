from datetime import datetime,timedelta
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse

from models import Employee,Project,Salary,ManPower,Lend,Shift
from forms import ManPowerForm

@login_required
def manpower_list(request):
	manpowers=ManPower.objects.filter(time_in__gt=datetime.today()-timedelta(days=7))
	return render(request,'manpower/manpower_list.html',{'manpowers':manpowers})

@login_required
def manpower_in_list(request,date=None,name=None,project=None):
	manpowers=ManPower.objects.filter(Q(time_in__gt=datetime.today()-timedelta(days=7))|Q(employee=name)|Q(project=project))
	return render(request,'manpower/manpower_in_list.html',{'manpowers':manpowers})

@login_required
def single_manpower_add(request):
	messages=''
	if request.method=='POST':
		single_form=ManPowerForm(request.POST)
		if single_form.is_valid():
			single_form.save(commit=False)
			single_form.working_time=timedelta(single_form.time_out-single_form.time_in)
			single_form.save()
			messages="Success!"
			return render(request,'manpower/manpower_single_add.html',{'single_form':single_form,'messages':messages,"projects":Projects.objects.all()})
		else:
			messages="it's exist, please try again!"
			return HttpResponse('')
	else:
		single_form=ManPowerForm()
	return render(request,'manpower/manpower_single_add.html',{'single_form':single_form,'messages':messages,'employees':Employee.objects.all(),"projects":Project.objects.all(),"shifts":Shift.objects.all()})


@login_required
def manpower_add(request):
	print request.user
	return render(request,'manpower/manpower_single_add.html',{})
	
@login_required
def multi_manpower_add(request):
	if request.method=="POST":
		print request.POST['multi_project_code']
		print request.POST['multi_date_from']
		print request.POST['multi_date_to']
		if request.POST['multi_project_code'] and request.POST['multi_date_from'] and request.POST['multi_date_to']:
			project_id=request.POST['multi_project_code']
			multi_date_from=request.POST['multi_date_from']
			multi_date_to=request.POST['multi_date_to']
#			multi_datetime_from=datetime.combine(multi_date_from,)
			try:
				project=Project.objects.get(id=project_id)
				print "project: ",project.id
				manpower=ManPower.objects.filter(project=project)
				#.filter(time_in__date=multi_date_from)
				for m in manpower:
					multi_datetime_in=datetime.combine(datetime.strptime(multi_date_to,"%Y-%m-%d"),time(hour=m.time_in.hour,minute=m.time_in.minute,second=m.time_in.second,microsecond=0))
					print datetime.strftime(multi_datetime_in,"%Y%m%h %H:%M:%S")
					if datetime.strftime(m.time_in,"%Y-%m-%d")==datetime.strftime(m.time_out,"%Y-%m-%d"):
						multi_datetime_out=datetime.combine(datetime.strptime(multi_date_to,"%Y-%m-%d"),datetime.strftime(m.time_out,"%H:%M:%S"))
					else:
						multi_datetime_out=datetime.combine(datetime.strptime(multi_date_to,"%Y-%m-%d")+datetime.timedelta(datetime.strftime(m.time_out,"%Y-%m-%d")-datetime.strftime(m.time_in,"%Y-%m-%d")),datetime.strftime(m.time_out,"%H:%M:%S"))
					print "in: %s" % (multi_datetime_in)
					print "out: %s" % (multi_datetime_out)
					new_manpower=Manpower.objects.create(employee=m.employee,project=m.project,time_in=multi_datetime_in,time_out=multi_datetime_out,lunch=m.lunch,shift=m.shift,working_time=m.working_time,remark=m.remark,create_by=request.user,is_checked=False,checked_by="",is_payed=False,payed_period="")
					new_manpower.save()
				return render(request,"manpower/manpower_multi_add.html",{"new_manpower":new_manpower})
			except Exception as e:
				print str(e)
				return single_manpower_add(request)
				#return HttpResponse("errors1")
		else:
			return HttpResponse("Please fill complete information,click <a href='/manpower/add/'>here</a> go back.")
	else:
		return single_manpower_add(request)

@login_required
def manpower_delete(request):
	pass

def getSearchResult(model,*orders,**wheres):
	ret=model.objects
	ret=ret.filter(**wheres)
	for order in orders:
		ret=ret.order_by(order)
	return ret
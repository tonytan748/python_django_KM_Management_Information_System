import datetime

from django.shortcuts import render
from django.db.models import Q
from models import *

def employee_list(request):
	employes=Employee.objects.all()
	return render(request,'man_power/employee_list.html',{'employes':employes})

def project_list(request):
	projects=Project.objects.all()
	return render(request,'man_power/project_list.html',{'projects':projects})

def manpower_list(request):
	if request.method=="POST":
		date=request.POST['date']
		project_id=request.POST['project_id']
		worker_id=request.POST['worker_id']
		results=ManPower.objects.get(Q(time_in__icontain=date)|Q(employee__icontain=worker_id)|Q(project__icontain=project_id))
		return render(request,'man_power/manpower_list.html',{'manpower_list':results})




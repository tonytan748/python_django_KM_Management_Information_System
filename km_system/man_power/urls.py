from django.urls import patterns,url

from models import *
import views

urlpatterns=patterns('',
	url(r'^employee_list/$',views.employee_list,name="employee_list"),
)

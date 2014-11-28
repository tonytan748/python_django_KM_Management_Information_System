from django.conf.urls import patterns,url
import views

urlpatterns=patterns('',
		url(r'^$',views.manpower_list,name="list"),
		url(r'^list/$',views.manpower_in_list,name="manpower_list"),
		
		url(r'^add/$',views.single_manpower_add,name="add"),
		url(r'^multi_add/$',views.multi_manpower_add,name="multi_add"),
#		url(r'^$',views.manpower_edit,name="edit"),
#		url(r'^$',views.manpower_delete,name="delete"),
)
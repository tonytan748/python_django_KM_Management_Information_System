from django.conf.urls import patterns,url

urlpatterns=patterns('sub_contractor.views',
	url(r'^$','subcon_list',name='list'),
	url(r'^add_item/$','add_item',name="add"),
	url(r'^del_item/(?P<pk>\d+)/$','del_item',name='delete'),
	url(r'^search_item/$','search_item',name='search'),
	url(r'^export_item/$','export_item_list',name='export'),

)

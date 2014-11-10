from django.conf.urls import patterns,url

urlpatterns=patterns('item.views',
	url(r'^$','ItemListView',name='list'),
	url(r'^add_item/$','add_item',name="add"),
	url(r'^del_item/(?P<pk>\d+)/$','del_item',name='delete'),
	url(r'^search_item/$','search_item',name='search'),
	url(r'^export_item/$','export_item_list',name='export'),


	url(r'^kinds/$','kinds_list',name='kinds'),
	url(r'^kinds_add/$','kinds_add',name='kindsadd'),
	url(r'^kinds_del/(?P<pk>\d+)/$','kinds_delete',name='kindsdelete'),
)

from django.conf.urls import patterns,url

urlpatterns=patterns('item.views',
	url(r'^$','ItemListView',name='list'),
	url(r'^add_item/$','add_item',name="add"),
	url(r'^del_item/(?P<pk>\d+)/$','del_item',name='delete'),
#	url(r'^search_item/$','search_supplier',name='search'),


#	url(r'^kinds/$','kinds',name='kinds'),
)

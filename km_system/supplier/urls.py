from django.conf.urls import patterns,url

urlpatterns=patterns('supplier.views',
	url(r'^$','SupplierListView',name='list'),
	url(r'^add_item/$','add_supplier',name="add"),
	url(r'^del_item/(?P<pk>\d+)/$','del_supplier',name='delete'),
	url(r'^search_item/$','search_supplier',name='search'),
)

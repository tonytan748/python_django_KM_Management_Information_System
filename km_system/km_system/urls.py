from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'km_system.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','django.contrib.auth.views.login',name='login'),
    url(r'^logout$','django.contrib.auth.views.logout'),

    url(r'^supplier/',include('supplier.urls',namespace='supplier')),
    url(r'^item/',include('item.urls',namespace='item')),

    url(r'^admin/', include(admin.site.urls)),
)


from django.conf.urls import patterns, include, url
from django.contrib import admin

from home import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newkmsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$','home.views.index'),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/',include('registration.backends.simple.urls')),
)

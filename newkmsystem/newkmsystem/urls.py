from django.conf.urls import patterns, include, url
from django.contrib import admin

def i18n_javascript(request):
    return admin.site.i18n_javascript(request)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'newkmsystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^$', 'home.views.index', name='home'),
					   
	url(r'^admin/jsi18n', i18n_javascript),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^accounts/',include('registration.backends.simple.urls')),

	url(r'^manpower/',include('manpower.urls',namespace="manpower")),
)

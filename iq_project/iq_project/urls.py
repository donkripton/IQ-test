from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'iq_project.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^iq_app/', include('iq_app.urls')),
	url(r'^admin/', include(admin.site.urls)),

)
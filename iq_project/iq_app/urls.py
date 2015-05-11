from django.conf.urls import patterns, url

from iq_app import views

urlpatterns = patterns('',
    
	url(r'^$', views.index, name='index'),
	url(r'^signup/$', views.signup, name='signup'),
    
    #user auth urls
	url(r'^login/$', views.user_login, name='login'),
	url(r'^home/$', views.home, name='home'),
	url(r'^iq_test/$', views.iq_test, name='iq_test'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^result_check/$', views.result_check, name='result_check'),
)
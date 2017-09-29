from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^friends$', views.friends),
	url(r'^friends/(?P<user_id>\d+)/viewprofile$', views.viewprofile),
	url(r'^friends/(?P<user_id>\d+)/removefriend$', views.removefriend),
	url(r'^friends/(?P<user_id>\d+)/addfriend$', views.addfriend),
	#(?P<user_id>\d+)
  ]
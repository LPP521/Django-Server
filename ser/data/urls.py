from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
	url('^index/', views.receive),
	url('^blog/',views.send),
)

from django.conf.urls import url
from django.contrib import auth
from . import views

urlpatterns = [
    url(r'^upload/$', views.upload_view, name='upload_view'),
    url(r'^$', views.index, name='index'),
#Only works for real IDs that are 1-4 digit long
    url(r'^upload/job/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/$', views.progress, name='progress'),
    url(r'^upload/job/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/results/$', views.result, name='results'),
    url(r'^upload/job/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/results/download$', views.download, name='download'),
]

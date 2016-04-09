from django.conf.urls import include, url
from upload import views
from . import views

urlpatterns = [
	#url(r'^upload/$', views.upload_view, name='upload_view'),
    #url(r'^$', views.index, name='index'),
    #url('^login/', views.login, name='login'),

#Only works for real IDs that are 1-4 digit long
    url(r'^upload/job/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/results/graph$', views.graph, name='graph'),
    url(r'^upload/job/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/results/json$', views.json_view, name='json_view'),
   # url(r'^upload/job/(?P<id>\d{1,4})/result/$', views.result, name='result')
]
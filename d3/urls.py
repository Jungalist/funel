from django.conf.urls import include, url
from upload import views
from . import views

urlpatterns = [
	url(r'^graphtest', views.graphtest, name='graphtest'),
	#url(r'^upload/$', views.upload_view, name='upload_view'),
    #url(r'^$', views.index, name='index'),
    #url('^login/', views.login, name='login'),

#Only works for real IDs that are 1-4 digit long
    url(r'^upload/job/(?P<id>\d{1,4})/graph$', views.graph, name='graph'),
   # url(r'^upload/job/(?P<id>\d{1,4})/result/$', views.result, name='result')
]
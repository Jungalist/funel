from django.conf.urls import include, url
from upload import views
from . import views

urlpatterns = [
    url(r'^upload/job/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/results/graph$', views.graph, name='graph'),
    url(r'^upload/job/(?P<id>\w{8}-\w{4}-\w{4}-\w{4}-\w{12})/results/json$', views.json_view, name='json_view'),
]
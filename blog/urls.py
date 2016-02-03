from django.conf.urls import url
from . import views

urlpatterns = [
#WHen entering the domain, use view post_list and name it post_list
    url(r'^$', views.post_list, name='post_list'),
]

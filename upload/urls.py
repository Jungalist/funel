from django.conf.urls import url
from . import views

urlpatterns = [
#when upload/ is present, show this view
    url(r'^upload/$', views.upload_view, name='upload_view'),
    url(r'^$', views.index, name='index'),
  #  url(r'^upload/success/$', views.success, name='success'),  
 # url(r'^uploaded/$', views.upload_view, name='uploaded_view'),
]

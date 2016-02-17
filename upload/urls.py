from django.conf.urls import url
from django.contrib import auth
from . import views

urlpatterns = [
#when upload/ is present, show this view
    url(r'^upload/$', views.upload_view, name='upload_view'),
    url(r'^$', views.index, name='index'),
    url('^login/', views.login, name='login')

   # url(r'^login/$', django.contrib.auth.views.login, name='login'),
   # url(r'^logout/$', django.contrib.auth.views.logout, name='logout')
  #  url(r'^upload/success/$', views.success, name='success'),  
 # url(r'^uploaded/$', views.upload_view, name='uploaded_view'),
]

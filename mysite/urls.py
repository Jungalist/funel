from django.conf.urls import include, url
from django.contrib import admin, auth
from upload.views import *
from d3.views import *
from newuser.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('upload.urls')),
    url(r'', include('d3.urls')),
    url('^', include('django.contrib.auth.urls')),
    url(r'^user/', show_jobs, name='jobs'),
    url('^login/$', login, name='login'),
    url(r'^login/email/(?P<token>[0-9a-z-]+)$', email_login),
    url(r'^contact/$', contact, name='contact'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
       
]

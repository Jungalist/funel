import os, sys, site


from django.core.wsgi import get_wsgi_application
sys.path.append('/home/seb/project/funel')
sys.path.append('/home/seb/project/funel/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


application = get_wsgi_application()



from django.contrib import admin
from .models import Upload
from d3.models import Graph

admin.site.register(Graph)
admin.site.register(Upload)

from django.shortcuts import render
from d3.scripts.convert import convert
from upload.models import Upload
from d3.models import Graph
from django.http import JsonResponse, HttpResponse
import simplejson as json


def graph(request, id):
	#TODO generate graph object in models
    g = Graph.objects.get(assoc_job_id=id)
    data = json.load(g.json_data)
    
    return render(request, 'd3/graph.html', {'json': data, 's': 's'})

#TODO allow downloads
def json_view(request, id):
	g = Graph.objects.get(assoc_job_id=id)
	data = json.load(g.json_data)
	return JsonResponse(data, content_type='application/json', safe=False)

   
    
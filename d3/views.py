from django.shortcuts import render
from d3.scripts.convert import convert
from upload.models import Upload
import json
from django.http import JsonResponse


def graphtest(request):
    json_data = open('/home/seb/project/djangoservice/media/media/co-prediction.json', 'r')
    print type(json_data)
    data1 = json.load(json_data) 
    data2 = json.dumps(json_data)
    return render(request, 'd3/graph.html', {'json': json_data})

def graph(request, id):
    u = Upload.objects.get(id=id)
	#find the path of the result file in DB and convert to json
    
    #make into proper id
    id = str(u.author.id) + '_' + str(id)
    convert(str(u.result.path), id)
    file = "/home/seb/project/djangoservice/media/graph/" + str(id) + '/' + "co-prediction.json"
   
    return render(request, 'd3/graph.html', {'json': file})

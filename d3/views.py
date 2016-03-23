from django.shortcuts import render
import json

def graph(request):
    return render(request, 'd3/graph.html', {})

def json(request):
    json_data = open('media/co-prediction.json')
    data1 = json.load(json_data) 
    data2 = json.dumps(json_data)
    return render(request, 'd3/graph.html', {'json': json_data})

from django.shortcuts import render

# Create your views here.
def graph(request):
    return render(request, 'd3/graph.html', {})

def json(request):
    

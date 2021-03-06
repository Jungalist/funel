import igraph
import sys, ast

pos = sys.argv[1]
user = sys.argv[2]
id = sys.argv[3]

links = []
names = []
maxX = 0
maxY = 0
minX = 0
minY = 0

with open(pos, 'r') as f:
#Get values from igraph.txt and split them into arrays
    name = f.readline()
    name = name.split()
    for n in name:
        names.append(n)

    lines = f.readlines()
    for p in lines:
        links.append(ast.literal_eval(p))
    
#apply igraph layout
bbox = (0, 0, 1024, 500)
g = igraph.Graph(links, bbox = bbox)

layout = g.layout("fr")
eigenvector_centrality = g.eigenvector_centrality()
betweeness = g.betweenness()

#extract coordinates and write them to json TODO hardcoded 1
pospath = "/home/seb/project/funel/media/graph/"+ str(user) + '_' + str(id) + "/positions.json"
with open(pospath, 'w+') as f:
    f.write('{"positions": [')
    
    for n in range(len(layout)):
    	#get min and max values for scaling, no switch statement in Python
    	if(layout[n][0] > maxX):
    		maxX = layout[n][0]
    	if(layout[n][0] < minX):
    		minX = layout[n][0]

    	if(layout[n][1] > maxY):
    		maxY = layout[n][1]
    	if(layout[n][1] < minY):
    		minY = layout[n][1]



        if(n < len(layout)-1):
            f.write('{"x": "' + str(layout[n][0]) + '", "y":"' + str(layout[n][1]) + '","eigenvector_centrality":"' 
                + str(eigenvector_centrality[n]) + '","betweeness":" ' + str(betweeness[n]) + '"},\n')
        else:
            f.write('{"x": "' + str(layout[n][0]) + '", "y":"' + str(layout[n][1]) + '","eigenvector_centrality":"' 
                + str(eigenvector_centrality[n]) + '","betweeness":" ' + str(betweeness[n]) + '"}\n')

    f.write('], "scales": [\n')
    f.write('{"maxX":"' + str(maxX) + '"},\n')
    f.write('{"minX":"' + str(minX) + '"},\n')
    f.write('{"maxY":"' + str(maxY) + '"},\n')
    f.write('{"minY":"' + str(minY) + '"}\n')
    f.write("]}")

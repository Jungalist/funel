import igraph
import sys, ast

pos = sys.argv[1]
id = sys.argv[2]

links = []
names = []

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
g = igraph.Graph(links)
layout = g.layout("kk")

#extract coordinates and write them to json
pospath = "/home/seb/project/funel/media/graph/1" + str(id) + "/positions.json"
with open(pospath, 'w+') as f:
    f.write('{"positions": [')
    for n in range(len(layout)):
        print n
        if(n < len(layout)-1):
            f.write('{"x": "' + str(layout[n][0]) + '", "y":"' + str(layout[n][1]) + '"},\n')
        else:
            f.write('{"x": "' + str(layout[n][0]) + '", "y":"' + str(layout[n][1]) + '"}\n')
    f.write("]}")

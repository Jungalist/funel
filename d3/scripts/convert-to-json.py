#A script to convert the raw data results from Funel to JSON ready for D3.js graph
import sys
def convert(inp, id):
    #Read the input from argument
    input = open(inp, 'r')

    #TODO from static
    outpath = "/home/seb/project/djangoservice/d3/static/graph/" + id + "co-prediction.json"
    output = open(outpath, 'w+')

    output.write('{\n"nodes":[\n')

    #TODO change to 2d array
    raw = []
    unique = []
    left = []
    right = []


    for line in input:
        word = line.split()
        raw.append(word[0])
        raw.append(word[1])
        left.append(word[0])
        right.append(word[1])

    #get unique
    for i in range(0, len(raw)-1):
        #for j in range(i+1, len(raw)):
        if raw[i] not in unique:
            unique.append(raw[i])
        #If not the last line, add comma, if it is the last line, no comma
        #TODO make more efficient, perhaps regex instead of ifing every time
        if i != len(raw)-2:
            output.write('{"name":' + '"' + str(raw[i]) + '"},\n')
        else:
    	   output.write('{"name":' + '"' + str(raw[i]) + '"}\n')

    output.write('],\n "links":[')

    for i in range(0, len(left)):
        if i != len(left)-1:
            output.write('{"source":' + str(unique.index(left[i])) + ', "target":' + str(unique.index(right[i])) + '},\n')
        else:
            output.write('{"source":' + str(unique.index(left[i])) + ', "target":' + str(unique.index(right[i])) + '}\n')
    	    
        
    output.write("]}")
    input.close()
    output.close()

    return outpath

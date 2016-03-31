#A script to convert the raw data results from Funel to JSON ready for D3.js graph
import sys, os
#import pdb; pdb.set_trace()


def convert(inp, id):
    #TODO from static
    if not os.path.exists("/home/seb/project/djangoservice/media/graph/" + str(id)):
        os.mkdir("/home/seb/project/djangoservice/media/graph/" + str(id))
    debug = open("/home/seb/project/djangoservice/media/graph/" + str(id) + "/debug.txt", 'w+')
    #TODO change to 2d array
        
    raw = []
    unique = []
    left = []
    right = []

    try:
        #Read the input from argument
        input = open(inp, 'r')
        outpath = "/home/seb/project/djangoservice/media/graph/" + str(id) + "/co-prediction.json"
        output = open(outpath, 'w+')
        

        output.write('{\n"nodes":[\n')

        


        for line in input:
            word = line.split()
            raw.append(word[0])
            raw.append(word[1])
            left.append(word[0])
            right.append(word[1])

        input.close()
        #get unique
        for i in range(0, len(raw)-1):
            #for j in range(i+1, len(raw)):
            if raw[i] not in unique:
                debug.write("raw[i] not in unique: " + str(raw[i]) + '\n')
                unique.append(raw[i])
            #If not the last line, add comma, if it is the last line, no comma
            #TODO make more efficient, perhaps regex instead of ifing every time
            #while i<len(raw):
                #normal line
            #end line

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

        output.close()
        debug.close()
        return str(outpath)


    except ValueError:
        debug.write('\n' + '\n' + "raw values: " + '\n')
        for value in raw:
            debug.write(value + ', ')

        debug.write('\n' + '\n' + "unique values: " + '\n')
        for value in unique:
            debug.write(value + ', ')


        debug.close()



    

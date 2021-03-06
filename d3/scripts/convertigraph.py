#A script to convert the raw data results from Funel to Python arrays readt for igraph
import sys, os
#import pdb; pdb.set_trace()


def convertigraph(inp, id):
    graphpath = "/home/seb/project/funel/media/graph/"
    
    #TODO from static
    if not os.path.exists(graphpath + str(id)):
        os.mkdir(graphpath + str(id))
    debug = open(graphpath + str(id) + "/debug.txt", 'w+')
    #TODO change to 2d array
        
    raw = []
    unique = []
    left = []
    right = []


    try:
        #Read the input from argument
        input = open(inp, 'r')
        outpath = graphpath + str(id) + "/igraph.txt"
        output = open(outpath, 'w+')


        for line in input:
            word = line.split()
            raw.append(word[0])
            raw.append(word[1])
            left.append(word[0])
            right.append(word[1])

        input.close()
        #output.write('[')
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
        for i in range(0, len(unique)-1):
            if i != len(unique)-2:
                output.write(str(unique[i]) + ' ')


        output.write('\n')

        for i in range(0, len(left)-1):
            output.write('(' + str(unique.index(left[i])) + ',' + str(unique.index(right[i])) + ')\n')
        print str(outpath)
        output.close()
        debug.close()
        return outpath


    except ValueError:
        debug.write('\n' + '\n' + "raw values: " + '\n')
        for value in raw:
            debug.write(value + ', ')

        debug.write('\n' + '\n' + "unique values: " + '\n')
        for value in unique:
            debug.write(value + ', ')


        debug.close()



    

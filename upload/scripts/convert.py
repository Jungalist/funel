#load data file
#read first line in for loop
#var = text until space
#var2 = text until carrige return
#add to stuff around
import sys


input = open("/home/seb/project/djangoservice/media/results/1_194/co-prediction.txt", 'r')
output = open("/home/seb/project/djangoservice/media/media/co-prediction.json", 'w+')

output.write('{\n"nodes":[\n')

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
	output.write('{"name":' + '"' + str(raw[i]) + '"},\n')

output.write('],\n "links":[')

for i in range(0, len(left)):
    output.write('{"source":' + str(unique.index(left[i])) + ', "target":' + str(unique.index(right[i])) + '},\n')
	    
    
output.write("]}")
input.close()
output.close()

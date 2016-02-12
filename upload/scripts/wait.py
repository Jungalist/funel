import time
print "Waiting"
time.sleep(5)
text_file = open("upload/scripts/Output.txt", "w")
text_file.write("Waited 5")
text_file.close()
print "Waited 5"


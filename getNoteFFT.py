from MusicAnalyzing import *
import numpy 
import os 

#note: with csv.DictWriter only 12 element from the arrray is storeed 
#numpy.savetxt will store all element/ about 20000 
#this file wll only run once to create a database with all fft for 
#88 piano note 

def writeCSVWithFft():
	for file in os.listdir("pianoWav"):
		if os.path.isdir("pianoWav"+"/"+file)==False:
			filename=file[9:-4]
			print(filename)
			fft=getFft("pianoWav"+"/"+file)
			numpy.savetxt("noteFft/%s.csv" %filename,fft)

writeCSVWithFft()


import numpy 
import csv 
import matplotlib.pyplot as plt
import scipy
from scipy.io import wavfile
from scipy.fftpack import fft
import os 

#learn from https://stackoverflow.com/questions/23377665/python-scipy-fft-wav-files
#modified for my own use 


def getFft(filename):
    (sampRate, data) = wavfile.read(filename) 
    try:
    	(frame,channel)=data.shape
    except:
    	(frame,)=data.shape
    	channel=1
    if channel == 2:
    	data = data.T[0] # transpose, then get the first channel
    trimData=[]
    for element in data:
    	trimData.append((element/2**8)*2-1) 
    fftList = fft(trimData)
    mid= len(fftList)/2 #fft symmetrical, only need half
    fftList=numpy.abs(fftList[:int(mid-1)])
    return fftList

def extractFftFromCSV(note):
	#correspondingly, change csv.DictReader to numpy.loadtxt
	fft=numpy.loadtxt("noteFft/"+note+".csv")
	return fft 

def getNoteName():
	noteList=[]
	for file in os.listdir("noteFft"):
		if os.path.isdir("noteFft/"+file)==False:
			filename=file[:-4]
			noteList.append(filename)
	return noteList


def testSimilarity(filename):
	noteName=getNoteName() #return list of note name
	sampleFft=getFft(filename) #return fft array for the file 
	numNote=len(noteName) #88
	mostLikelyNote=""
	mostLikelyPoss=0
	similarity=[]
	for i in range(0,numNote):
		note=noteName[i]
		arrayFft=extractFftFromCSV(note)
		arraySize=arrayFft.shape[0]
		sampleSize=sampleFft.shape[0]
		print(sampleSize,arraySize)
		cropSize=min(arraySize,sampleSize)
		poss=1-scipy.spatial.distance.cosine(sampleFft[:cropSize],
											arrayFft[:cropSize])
		similarity.append([note,poss])
		if poss >mostLikelyPoss:
			mostLikelyPoss=poss
			mostLikelyNote=noteName[i]
	#print(similarity)
	print(mostLikelyNote)
	return mostLikelyNote
#test.D4
#original=Bb5
#same=D5
#standard=Bb5 
#small=D5
testSimilarity("test4.C4.D4.E4.wav")



################################################

def plotGraph(path): 
    sampRate,data=wavfile.read(path)
    data=data/(2.**15)
    try:
    	(frame,channel)=data.shape
    except:
    	(frame,)=data.shape
    	channel=1
    if channel == 1:
    	trimData=data
    else:
    	trimData=data[:,0]
    plt.clf() #clear current graph

    waveX=numpy.arange(0,frame,1)/sampRate *1000
    waveY=trimData

    # wave
    plt.figure(figsize=(10,2))
    plt.plot(waveX,waveY)
    # plt.axis([0, frame, -0.5, 0.5])
    plt.xlabel("time [sample]")
    plt.ylabel("amplitude")
    fileName=path[:-4]
    plt.savefig(fileName+".png")



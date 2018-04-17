import pyaudio 
import pygame
import wave
import sys 

def recordWav(path): 
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 5
	 
	p = pyaudio.PyAudio()
	 
	# start Recording
	stream = p.open(format=FORMAT, channels=CHANNELS,
					rate=RATE, input=True,
					frames_per_buffer=CHUNK)
	print ("recording...")
	frames = []
	 
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
		data = stream.read(CHUNK)
		frames.append(data)
	print ("finished recording")
	 
	# stop Recording
	stream.stop_stream()
	stream.close()
	p.terminate()
	 
	waveFile = wave.open(path, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(p.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()


def playWav(path):
	chunk=1024
	wavFile=wave.open(path)
	p=pyaudio.PyAudio()

	stream=p.open(format=p.get_format_from_width(wavFile.getsampwidth()),\
				channels=wavFile.getnchannels(), rate=wavFile.getframerate(),output=True)
	data=wavFile.readframes(chunk)

	while data!="":
		stream.write(data)
		data=wavFile.readframes(chunk)

	stream.close()
	p.terminate

##########################################################################
#### Open File Browser ####
def openFileBrowserWav():
	pygame.mixer.init()  # initializing the mixer
	import tkinter
	from tkinter import filedialog
	root = tkinter.Tk()
	root.withdraw()
	root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
											   filetypes=(("Audio Files", ".wav .ogg"),   ("All Files", "*.*")))
	return root.filename

def openFileBrowserPic():
	pygame.mixer.init()  # initializing the mixer
	import tkinter
	from tkinter import filedialog
	root = tkinter.Tk()
	root.withdraw()
	root.filename = filedialog.askopenfilename(initialdir="/", title="Select file",
											   filetypes=(("jpeg files", "*.jpg"),("PNG file","*.png")))
	return root.filename
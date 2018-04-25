import pyaudio 
import pygame
import wave
import sys 

def recordWav(path): 
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	CHUNK = 1024
	RECORD_SECONDS = 3
	 
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

def within(left,down,width,height,x,y):
	return left < x < left+width and down < y < down +height


def displayText(screen,text,points,fontColor,font):
	(a,b,c,d)=points
	#a,b=coordinates/ c=width, d=height
	myFont = font
	textSurface = myFont.render(text, True, fontColor)
	textRect1 = textSurface.get_rect()
	textRect1.center = (a + c//2, b + d//2)
	screen.blit(textSurface, textRect1)
	
def displayTextAlignLeft(screen,text,a,b,fontColor,font):
	textSurface=font.render(text,True,fontColor)
	textRect1=textSurface.get_rect()
	screen.blit(textSurface,(a,b+5))

############## init for all class ######################################
def initColor(self):
	self.white = (254,251,249)
	self.black= (0,0,0)
	self.grey=(99,99,112)
	self.lightBlue=(79,160,156)
	self.darkBlue=(18,83,104)
	self.deepBlue=(70,130,180)
	self.lightRed=(251,62,46)
	self.darkRed=(106,26,26)

	
def loadFont(self):
	self.regularFont=pygame.font.SysFont('harlowsolid',90)
	self.titleFont=pygame.font.SysFont('harlowsolid',70)
	self.btnFont=pygame.font.SysFont("arial",20)
	self.settingFont=pygame.font.SysFont('harlowsolid',30)
	font=pygame.font.get_fonts()

def initPic(self):
	self.bg=pygame.image.load("2.jpg")
	self.backBtnImage=pygame.image.load("back.png")
	self.mtsIcon=pygame.image.load("musicToSheet.png")
	self.mmIcon=pygame.image.load("musicMaking.png")
	self.trebleClef=pygame.image.load("icon/trebleClef.png")
	self.bassClef=pygame.image.load("icon/bassClef.png")
	self.clefPics=[self.trebleClef,self.bassClef]
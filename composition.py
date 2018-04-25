from music21 import *
from pygame import *

class Composition(object):
	def __init__(self,clef,beat,title,screen):
		self.screen=screen
		self.clef,self.beat,self.title=clef,beat,title
		self.measurePerPage=16
		self.composition = self.initPage()
		self.horiLoc=[374,589,804,1019,1234]
		self.verLoc=[261.5,407.5,553.5,698.5]
		self.tnoteList=["C4","D4","E4","F4","G4","A4","B4","C5","D5","E5","F5","G5","A5"]
		self.bnoteList=["E2","F2","G2","A2","B2","C3","D3","E3","F3","G3","A3","B3","C4"]
		self.initNotePic()
		self.verDiv=5
		self.horiDiv=215
		self.currentPage=1
		self.compNoteList=[[] for i in range(0,self.measurePerPage)]
		self.compNoteOffset=[[] for i in range(0,self.measurePerPage)]
		self.midiName="%s.mid" %self.title

	def initNotePic(self):
		self.n1=image.load("icon/whole-note.png")
		self.n2=image.load("icon/half-note.png")
		self.n4= image.load("icon/4th-note.png")
		self.n8=image.load("icon/8th-note.png")
		self.n16=image.load("icon/16th-note.png")
		self.n32=image.load("icon/32nd-note.png")
		self.r1=image.load("icon/whole-rest.png")
		self.r2=image.load("icon/whole-rest.png")
		self.r4=image.load("icon/quarter-rest.png")
		self.r8=image.load("icon/8th-rest.png")
		self.r16=image.load("icon/16th-rest.png")
		self.r32=image.load("icon/32nd-rest.png")

	def getTitle(self):
		return self.title

	def initPage(self):
		#return a big stream with 16 stream in it 
		comp=stream.Stream()
		for i in range(self.measurePerPage):
			comp.append(stream.Stream())
		return comp

	def addPage(self):
		#add 16 more stream to the big stream=comp 
		for i in range(self.measurePerPage):
			self.composition.append(stream.Stream())
			self.compNoteList.append([])
			self.compNoteOffset.append([])

	def addNote(self,pos):
		(x,y)=pos
		col=self.getHorizontalLoc(x)
		(line,space)=self.getVerticalLoc(y)
		if line!=-1 and space!=-1 and col!=-1:
			measure=self.measurePerPage*(self.currentPage-1)+4*line+col
			if self.clef=="Treble Clef":
				#13 note
				noteName=self.tnoteList[space]
				self.compNoteList[measure].append(space)
				self.composition[measure].append(note.Note(noteName))
			elif self.clef=="Base Clef":
				noteName=self.bnoteList[space]
				self.compNoteList[measure].append(noteNme)
				self.composition[measure].append(note.Note(noteName))

	def changeTune(self,dt,pos):
		(x,y)=pos
		col=self.getHorizontalLoc(x)
		(line,space)=self.getVerticalLoc(y)
		if line!=-1 and space!=-1 and col!=-1:
			measure=self.measurePerPage*(self.currentPage-1)+4*line+col
			noteIndex=self.getNoteOrder(measure,x,y)
			selectNote=self.composition[measure][noteIndex]
			if dt==1:
				selectNote.transpose("M1",inPlace=True)
			elif dt==-1:
				selectNote.transpose("B1",inPlace=True)


	def changeDuration(self,dt,pos):
		(x,y)=pos
		col=self.getHorizontalLoc(x)
		(line,space)=self.getVerticalLoc(y)
		if line!=-1 and space!=-1 and col!=-1:
			measure=self.measurePerPage*(self.currentPage-1)+4*line+col
			noteIndex=self.getNoteOrder(measure,x,y)
			selectNote=self.composition[measure][noteIndex]
			if dt==1:
				selectNote.quaterLength+=0.5
			elif dt==-1:
				selectNote.quaterLength-=0.5

	def getHorizontalLoc(self,x):
		col=-1
		for i in range(0,len(self.horiLoc)-1):
			if self.horiLoc[i]<=x<=self.horiLoc[i+1]:
				col=i
		return col

	def getVerticalLoc(self,y):
		#self.verLoc=[263.5,407.5,553.5,698.5]
		#13 division and 13 places to add note 
		line=-1
		space=-1
		for i in range(0,len(self.verLoc)):
			if self.verLoc[i]-13*self.verDiv<=y<=self.verLoc[i]:
				line=i 

				for j in range(13):
					if self.verLoc[line]-(j+2)*self.verDiv<=y<=self.verLoc[line]-j*self.verDiv:
						space=j
		return (line,space)

	def getNoteOrder(self,measure,pos):

		return noteIndex

	def getNearestLoc(self):
		pass

	def loadComp(self):
		self.composition.write("midi",self.midiName)
		self.composition.show("text")

	def play(self,delta):
		self.composition.write("midi",self.midiName)
		mixer.music.load(self.midiName)
		if delta==1:
			mixer.music.play()
		elif delta==-1:
			mixer.music.pause()

	def blitNote(self):
		#self.compNoteOffset[measure].append(self.composition[measure][-1].quaterLength)
		for measure in range(0,self.currentPage*16):
			if self.clef=="Treble Clef":
				for note in (0,len(self.compNoteList[measure])):
					self.screen.blit(self.n16,(500,323))







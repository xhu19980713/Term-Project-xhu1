import pygame
from Accessories import *
class MusicToSheet(object):
	def __init__(self,screen,mode):
		self.screen=screen
		self.mode=mode
		self.fps=50

	def init(self):
		initColor(self)
		loadFont(self)
		initPic(self)
		self.mtsMode="result"
		self.mtsDelay=0
		self.pos=(-1,-1)
		self.width=1280
		self.height=720
		self.musicToSheetButton()
		self.resultButton()

		self.isSaved=True #by default: False 
		self.discard=False

		self.duration=0


	def musicToSheetButton(self):
		#circle buttons: circle(Surface, color, pos, radius, width=0)
		cx1=400
		cy1=400
		gap=80
		radius=175
		self.importFile=[self.lightBlue,cx1,cy1,radius]
		self.recordMusic=[self.lightBlue,self.width-cx1,cy1,radius]
		self.musicToSheetBtnList=[self.importFile,self.recordMusic]

	def recordingSettingButton(self):
		durationBtn=[590,200,200,40,self.lightBlue]
		recordBtn=[600,500,180,40,self.lightBlue] #better be a circle

	def resultButton(self):
		h=60
		w=100
		xs=60
		self.upPanel=[0,0,1280,h,self.lightBlue]
		self.saveBtn=[xs,0,w,h,self.lightBlue,"Save"]
		self.discardBtn=[xs+w,0,w,h,self.lightBlue,"Discard"]
		self.helpBtn=[1280-2*w,0,w,h,self.lightBlue,"Help"]
		self.libraryBtn=[1280-w,0,w,h,self.lightBlue,"Library"]
		self.exportBtn=[xs+w*4,0,w,h,self.lightBlue,"Export"]
		self.playBtn=[xs+2*w,0,w,h,self.lightBlue]
		self.pauseBtn=[xs+3*w,0,w,h,self.lightBlue]
		self.resultBtnList=[self.upPanel,self.saveBtn,self.discardBtn,
							self.helpBtn,self.libraryBtn,self.exportBtn,
							self.playBtn,self.pauseBtn]
		self.playIcon=[(295,15),(325,30),(295,45),self.black]
		self.pauseIcon=[(390,15,15,30),(415,15,15,30),self.black]


############ mouse Activity ##########################################
	def mousePressedMTS(self,x,y):
		if self.mode=="musicToSheet":
			for btn in self.musicToSheetBtnList:
				if (x-btn[1])**2+(y-btn[2])**2 <= btn[3]**2:
					btn[0]=self.deepBlue 

	def mouseReleasedMTS(self,x,y):
		if self.mode=="musicToSheet" and self.mtsDelay>=1:
			for btnNum in range(0,len(self.musicToSheetBtnList)):
				cx=self.musicToSheetBtnList[btnNum][1]
				cy=self.musicToSheetBtnList[btnNum][2]
				r=self.musicToSheetBtnList[btnNum][3]
				color=self.musicToSheetBtnList[btnNum][0]
				if (x-cx)**2+(y-cy)**2 <= r**2:
					color=self.lightBlue
					if btnNum==0:
						self.path=openFileBrowserWav()
						if self.path!=None and self.path!="":
							self.mode="analyzing"
					else:
						self.mode="recording"

	def mouseReleasedBack(self,x,y):
		(width,height)=self.backBtnImage.get_size()
		if 10<=x<=width and 5<=y<=height:
			if self.mtsMode=="recording":
				self.mtsMode="select"
			elif self.mtsMode=="analyzing":
				self.mtsMode="result"
			elif self.mtsMode=="result" and (self.isSaved==True or self.abandon==True):
				self.mode="start"


	def mouseMotionMTS(self,x,y):
		if self.mode=="musicToSheet":
			for btn in self.musicToSheetBtnList:
				if (x-btn[1])**2+(y-btn[2])**2 <= btn[3]**2:
					btn[0]=self.darkBlue 
				else:
					btn[0]=self.lightBlue
	def mousePressed(self,x,y):
		self.mousePressedMTS(x,y)

	def mouseReleased(self,x,y):
		self.mouseReleasedBack(x,y)
		self.mouseReleasedMTS(x,y)

	def mouseMotion(self,x,y):
		self.mouseMotionMTS(x,y)

############ key activity ################################

	def keyPressed(self, keyCode, modifier):
		pass 
		
	def keyReleased(self, keyCode, modifier):
		pass
	def timerFired(self, dt):
		if self.mode=="musicToSheet":
			self.mtsDelay+=1
################################################

	def redrawSelect(self):
		if self.mtsMode=="select":
			for btn in self.musicToSheetBtnList:
				pygame.draw.circle(self.screen,btn[0],btn[1:3],btn[3])
			self.screen.blit(self.backBtnImage,(10,5))

	def redrawRecording(self,):
		if self.mtsMode=="recording":
			pass

	def redrawResult(self):
		if self.mtsMode=="result":
			for btn in self.resultBtnList:
				pygame.draw.rect(self.screen,btn[4],btn[:4])
				pygame.draw.rect(self.screen,self.black,btn[:4],2)
			for btn in self.resultBtnList[1:6]:
				displayText(self.screen,btn[5],btn[:4],self.black,self.btnFont)
			self.screen.blit(self.backBtnImage,(10,5))
			pygame.draw.polygon(self.screen,self.playIcon[3],self.playIcon[:3])
			pygame.draw.rect(self.screen,self.pauseIcon[2],self.pauseIcon[0])
			pygame.draw.rect(self.screen,self.pauseIcon[2],self.pauseIcon[1])


	def redrawAll(self):
		self.redrawSelect()
		self.redrawRecording()
		self.redrawResult()

	def returnMode(self):
		return self.mode 

	def run(self):
		clock = pygame.time.Clock()
		# stores all the keys currently being held down
		self._keys = dict()
		# call game-specific initialization
		self.init()

		playing = True
		while playing and self.mode=="musicToSheet":
			time = clock.tick(self.fps)
			self.timerFired(time)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.mousePressed(*(event.pos))
					self.currentPos=event.pos
				elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					self.mouseReleased(*(event.pos))
					self.pos=event.pos
				elif (event.type == pygame.MOUSEMOTION and
					  event.buttons == (0, 0, 0)):
					self.mouseMotion(*(event.pos))
				elif event.type == pygame.KEYDOWN:
					self._keys[event.key] = True
					self.keyPressed(event.key, event.mod)
				elif event.type == pygame.KEYUP:
					self._keys[event.key] = False
					self.keyReleased(event.key, event.mod)
				elif event.type == pygame.QUIT:
					playing = False
			self.redrawAll()
			pygame.display.flip()
		self.mode="start"
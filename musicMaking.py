from music21 import *
from pygame import *
from Accessories import *
from composition import *

class MusicMaking(object):
	clefList=["Treble Clef","Bass Clef"]

	def __init__(self,screen,mode):
		self.screen=screen
		self.mode=mode
		self.fps=50

	def init(self):
		initColor(self)
		loadFont(self)
		initPic(self)
		self.white=(255,255,255)
		self.mmMode="mmSetting"
		#mmModeList=["mmSetting","creating"]
		self.display=Rect(300,60,980,660)
		self.subsurface=self.screen.subsurface(self.display)
		self.pageNum=1
		self.musicMakingButton()
		self.mmSetting()
		self.isSaved=True #by default: False
		self.discard=False
		self.pos=(-1,-1)

		self.clefChoice=""
		self.isClefChoosen=False
		self.writeTitle=False
		self.title=""
		self.beat=4
		self.currentComp=None
		self.compList=[]
		self.compList.append(self.currentComp)
		self.totalPage=1





########### btn list ######################################

	def musicMakingButton(self):
		h=60
		w=100
		xs=60
		self.upPanel=[0,0,1280,h,self.lightBlue]
		self.panel=[0,60,300,710,self.lightBlue]
		self.saveBtn=[xs,0,w,h,self.lightBlue,"Save"]
		self.discardBtn=[xs+w,0,w,h,self.lightBlue,"Discard"]
		self.helpBtn=[1280-3*w,0,w,h,self.lightBlue,"Help"]
		self.settingBtn=[1280-2*w,0,w,h,self.lightBlue,"Setting"]
		self.libraryBtn=[1280-w,0,w,h,self.lightBlue,"Library"]
		self.exportBtn=[xs+w*4,0,w,h,self.lightBlue,"Export"]
		self.addNoteBtn=[0,80,300,h,self.lightBlue,"Note"]
		#self.addRestBtn=[0,130,300,h,self.lightBlue,"Rest"]
		self.page=[100+33,720-h,33,h,self.lightBlue,""]
		self.turnLeft=[100,720-h,33,h,self.lightBlue,"<"]
		self.turnRight=[100+33*2,720-h,33,h,self.lightBlue,">"]
		self.playBtn=[xs+2*w,0,w,h,self.lightBlue]
		self.pauseBtn=[xs+3*w,0,w,h,self.lightBlue]
		self.noticeBoard=[20,200,260,470,self.white]

		self.mmBtnList=[self.upPanel,self.panel,self.saveBtn,self.discardBtn,self.helpBtn,self.settingBtn,self.libraryBtn,
						self.exportBtn,self.addNoteBtn,self.page,self.turnLeft,self.turnRight,
						self.playBtn,self.pauseBtn,self.noticeBoard]
		self.mmBtnList2=[self.saveBtn,self.discardBtn,self.helpBtn,self.settingBtn,self.libraryBtn,
						self.exportBtn,self.addNoteBtn,self.turnLeft,self.turnRight,
						self.playBtn,self.pauseBtn]

		self.playIcon=[(295,15),(325,30),(295,45),self.black]
		self.pauseIcon=[(390,15,15,30),(415,15,15,30),self.black]


	def mmSetting(self):
		self.nameBtn=[200,200,300,40,self.lightBlue]
		self.trebleClefBtn=[200,300,100,40,self.lightBlue,"Treble Clef"]
		self.bassClefBtn=[330,300,100,40,self.lightBlue,"Bass Clef"]
		self.doneBtn=[1220,0,60,55,self.lightBlue,"Done"]
		self.mmSettingBtnList=[self.nameBtn,self.trebleClefBtn,self.bassClefBtn,self.doneBtn]
		self.clefBtnList=[self.trebleClefBtn,self.bassClefBtn]

####################################################################################

	def updateScoreSheet(self):
		if self.mmMode=="creating":
			if self.clefChoice!="":
				for i in range(0,len(self.clefList)):
					if self.clefList[i]==self.clefChoice:
						self.screen.blit(self.clefPics[i],(302,170))
			
######## mouse activity ################################################

	def mouseReleasedBack(self,x,y):
		(width,height)=self.backBtnImage.get_size()
		if 10<=x<=10+width and 5<=y<=5+height:
			if self.mmMode=="mmSetting":
				self.mode="start"
			elif self.mmMode=="mmLibrary":
				self.mmMode="creating"
			elif self.mmMode=="creating" and (self.isSaved==True or self.discard==True):
				self.mode="start"

	def mouseReleasedMmSetting(self,x,y):
		if self.mmMode=="mmSetting":
			if within(1220,0,60,55,x,y) and self.isClefChoosen and self.title!="":
				self.mmMode="creating"
				self.currentComp=Composition(self.clefChoice,self.beat,self.title,self.screen)
			else:
				for btn in self.clefBtnList:
					if within(btn[0],btn[1],btn[2],btn[3],x,y) and not self.isClefChoosen:
						self.clefChoice=btn[5]
						btn[4]=self.darkBlue
						self.isClefChoosen=True
					elif within(btn[0],btn[1],btn[2],btn[3],x,y) and self.isClefChoosen:
						self.isClefChoosen=False 
						self.clefChoice=""
						btn[4]=self.lightBlue
			if within(200,200,200,40,x,y) and not self.writeTitle:
				self.writeTitle=True
				self.nameBtn[4]=self.darkBlue
			elif within(200,200,200,40,x,y) and self.writeTitle:
				self.writeTitle=False
				self.nameBtn[4]=self.lightBlue

	def mouseReleasedCreating(self,x,y):
		if self.mmMode=="creating":
			self.mouseReleasedAdd(x,y)
			btn=self.exportBtn
			if within(btn[0],btn[1],btn[2],btn[3],x,y):
				image.save(self.subsurface,"%s page %d.png" %(self.title,self.pageNum))
			btn=self.playBtn
			if within(btn[0],btn[1],btn[2],btn[3],x,y):
				self.currentComp.play(1)
			btn=self.pauseBtn		
			if within(btn[0],btn[1],btn[2],btn[3],x,y):
				self.currentComp.play(-1)
			btn=self.turnRight
			if within(btn[0],btn[1],btn[2],btn[3],x,y):
				self.pageNum+=1
				self.totalPage+=1
				self.currentComp.addPage()
				self.updateScoreSheet()
			btn=self.turnLeft
			if within(btn[0],btn[1],btn[2],btn[3],x,y) and self.pageNum>=1:
				self.pageNum-=1

	def mouseReleasedAdd(self,x,y):
		if within(300,60,980,660,x,y):
			self.currentComp.addNote((x,y))
			self.currentComp.loadComp()


	def mouseMotion(self,x,y):
		if self.mmMode=="mmSetting":
			pass
		elif self.mmMode=="creating":
			for btn in self.mmBtnList2:
				if within(btn[0],btn[1],btn[2],btn[3],x,y):
					btn[4]=self.darkBlue
				else:
					btn[4]=self.lightBlue

	def mouseReleased(self,x,y):
		self.mouseReleasedBack(x,y)
		self.mouseReleasedMmSetting(x,y)
		self.mouseReleasedCreating(x,y)
	

	def mousePressed(self,x,y):
		pass

######## key activity ##################################################
	def keyPressed(self, keyCode, modifier):
		pass 
		
	def keyReleased(self, keyCode, modifier):
		if self.mmMode=="mmSetting":
			if self.writeTitle:
				if 44<=keyCode<=69 or 97<=keyCode<=122 or keyCode==32:
					self.title+=chr(keyCode)
				elif keyCode==13:
					self.writeTitle=False
				elif keyCode==8:
					self.title=self.title[:-1]
		elif self.mmMode=="creating":
			if keyCode==273:  #up
				self.currentComp.changeTune(1,self.pos)
			elif keyCode==274: #down
				self.currentComp.changeTune(-1,self.pos)
			elif keyCode==276: #left
				self.currentComp.changeDuration(-1,self.pos)
			elif keyCode==275: #right
				self.currentComp.changeDuration(1,self.pos)

#######################################################################
	def timerFired(self, dt):
		pass 

######  redraw ############################################

#bug1: will always draw mmSetting 
	def redrawMmSetting(self):
		if self.mmMode=="mmSetting":
			self.screen.blit(self.backBtnImage,(10,5))
			for btn in self.mmSettingBtnList:
				if len(btn) >5:
					pygame.draw.rect(self.screen,btn[4],btn[:4])
					displayText(self.screen,btn[5],btn[:4],self.black,self.btnFont)
				else:
					pygame.draw.rect(self.screen,btn[4],btn[:4])
					displayText(self.screen,self.title,btn[:4],self.black,self.btnFont)
			displayTextAlignLeft(self.screen,"Input Composition Name Here:",200,140,self.black,self.settingFont)
			displayTextAlignLeft(self.screen,"Choose Your Clef",200,250,self.black,self.settingFont)


	def redrawCreating(self):
		if self.mmMode=="creating":
			for btn in self.mmBtnList:
				pygame.draw.rect(self.screen,btn[4],btn[:4])
				pygame.draw.rect(self.screen,self.black,btn[:4],2)
			for btn in self.mmBtnList[2:12]:
				displayText(self.screen,btn[5],btn[:4],self.black,self.btnFont)
			displayText(self.screen,"%d" %self.pageNum,[100+33,720-60,33,60],self.black,self.btnFont)
			self.screen.blit(self.backBtnImage,(10,5))
			# for btn in self.mmBtnList:
			# 	pygame.draw.rect(self.screen,self.black,btn[:4],2)
			pygame.draw.polygon(self.screen,self.playIcon[3],self.playIcon[:3])
			pygame.draw.rect(self.screen,self.pauseIcon[2],self.pauseIcon[0])
			pygame.draw.rect(self.screen,self.pauseIcon[2],self.pauseIcon[1])
			pygame.draw.rect(self.screen,self.white,[300,60,980,660])
			displayText(self.screen,self.title,[300,70,980,100],self.black,self.titleFont)
			displayText(self.screen,"page %d"%self.pageNum,[1100,140,120,30],self.black,self.btnFont)
			self.updateScoreSheet()


	def redrawAll(self):
		self.redrawMmSetting()
		self.redrawCreating()


####################################################################################################
	def returnMode(self):
		return self.mode

	def run(self):
		clock = pygame.time.Clock()
		# stores all the keys currently being held down
		self._keys = dict()
		# call game-specific initialization
		self.init()

		playing = True
		while playing and self.mode=="musicMaking":
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
#bug2: close window==> go back to main menu instead of close 
		self.mode="start"

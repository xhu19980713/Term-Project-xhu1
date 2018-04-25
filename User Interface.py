import pygame 
import os
from Accessories import *
from musicMaking import *
from musicToSheet import *


# TP launcher 
# main framwork is copied from my Hack112 project
# cited https://github.com/xhu19980713/Final-Hack112.git


class Muse(object):
	def __init__(self, width, height, fps=50, title="Muse"):
		self.width = width
		self.height = height
		self.fps = fps
		self.title = title
		pygame.init()	

### Main Framework ######
#########################
	def init(self):
		initColor(self)
		loadFont(self)
		initPic(self)
		self.path = None

		#self.modeList=["start","musicToSheet","musicMaking",\
					   # "analyzing","recording","mmSetting"]
		self.mode="start"
		self.startButtton()
		self.mtsDelay=0

	def startButtton(self):
		gap=51
		width=326
		height=300
		startX=100
		startY=350
		self.musicToSheetBtn=[startX,startY,width,height,self.lightBlue,\
		                     "musicToSheet"]
		self.musicMakingBtn=[startX+gap*2+width*2,startY,width,height,self.lightBlue,\
		                     "musicMaking"]
		self.startBtnList=[self.musicToSheetBtn,self.musicMakingBtn]



	def launch(self,screen):
		if self.mode=="musicMaking":
			musicMaking=MusicMaking(screen,self.mode)
			musicMaking.run()
			self.mode=musicMaking.returnMode()
		elif self.mode=="musicToSheet":
			musicToSheet=MusicToSheet(screen,self.mode)
			musicToSheet.run()
			self.mode=musicToSheet.returnMode()
		elif self.mode=="start":
			self.redrawAll(screen)


### Mouse Pressed ###
	def mousePressedStart(self,x,y):
		if self.mode=="start":
			for btn in self.startBtnList:
				if within(btn[0],btn[1],btn[2],btn[3],x,y):
					btn[4]=self.deepBlue


	def mousePressed(self,x,y):
		self.mousePressedStart(x,y)

#### MouseReleased ####
	def mouseReleasedStart(self,x,y):
		if self.mode=="start":
			for btn in self.startBtnList:
				if within(btn[0],btn[1],btn[2],btn[3],x,y):
					btn[4]=self.lightBlue
					self.mode=btn[5]


	def mouseReleased(self,x,y):
		self.mouseReleasedStart(x,y)

#### MouseMotion ####
	def mouseMotionStart(self,x,y):
		if self.mode=="start":
			for btn in self.startBtnList:
				if within(btn[0],btn[1],btn[2],btn[3],x,y):
					btn[4]=self.darkBlue
				else:
					btn[4]=self.lightBlue

	def mouseMotion(self, x, y):
		self.mouseMotionStart(x,y)

### Key ###
	def keyPressed(self, keyCode, modifier):
		pass 
		
	def keyReleased(self, keyCode, modifier):
		pass
#### timerFried ####

	def timerFired(self, dt):
		pass

### redraw ####
	def redrawStart(self,screen):
		if self.mode=="start":
			displayTextAlignLeft(screen,"Welcome to Muse",\
					self.width//8,self.height//5,self.black,self.regularFont)
			for btn in self.startBtnList:
				pygame.draw.rect(screen, btn[4], btn[:4])
			screen.blit(self.mtsIcon,(100,350))
			screen.blit(self.mmIcon,(326*2+51*2+140,370))


	def redrawAll(self, screen):
		self.redrawStart(screen)
	

### RUN FUNCTION ###

	def isKeyPressed(self, key):
		#return whether a specific key is being held
		return self._keys.get(key, False)


	def run(self):
		clock = pygame.time.Clock()
		screen = pygame.display.set_mode((self.width, self.height))
		# set the title of the window
		pygame.display.set_caption(self.title)

		# stores all the keys currently being held down
		self._keys = dict()

		# call game-specific initialization
		self.init()

		playing = True
		while playing:
			time = clock.tick(self.fps)
			self.timerFired(time)
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					self.mousePressed(*(event.pos))
					self.currentPos=event.pos
				elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					self.mouseReleased(*(event.pos))
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
			screen.blit(self.bg,(0,0))
			self.launch(screen)
		
			pygame.display.flip()

		pygame.quit()

def main():
	muse = Muse(1280,720)
	muse.run()

if __name__ == '__main__':
	main()
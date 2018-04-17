import pygame 
import os
from Accessories import *
from Button import *

class MusicReader(object):

	def initColor(self):
		self.white = (254,251,249)
		self.black= (0,0,0)
		self.grey=(99,99,112)
		self.lightBlue=(79,160,156)
		self.darkBlue=(18,83,104)
		self.deepBlue=(70,130,180)
		self.lightRed=(251,62,46)
		self.darkRed=(106,26,26)
	
	def within(self,left,down,width,height,x,y):
		return left < x < left+width and down < y < down +height
		
	def loadFont(self):
		self.regularFont=pygame.font.SysFont('harlowsolid',90)
		font=pygame.font.get_fonts()
		print(font)

### Main Framework ######
#########################
	def init(self):
		self.path = None
		self.initColor()
		self.loadFont()
		self.modeList=["start","musicToSheet","sheetToMusic","musicMaking",\
					   "analyzing","recording"]
		self.mode="start"
		allButton(self)
		self.mtsDelay=0
		self.bg=pygame.image.load("2.jpg")
		self.backBtnImage=pygame.image.load("back.png")
		self.mtsIcon=pygame.image.load("musicToSheet.png")
		self.stmIcon=pygame.image.load("sheetToMusic.png")
		self.mmIcon=pygame.image.load("musicMaking.png")

### Mouse Pressed ###
	def mousePressedStart(self,x,y):
		if self.mode=="start":
			for btn in self.startBtnList:
				if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
					btn[4]=self.deepBlue 

	def mousePressedMTS(self,x,y):
		if self.mode=="musicToSheet":
			for btn in self.musicToSheetBtnList:
				if (x-btn[1])**2+(y-btn[2])**2 <= btn[3]**2:
					btn[0]=self.deepBlue 

	def mousePressedSTM(self,x,y):
		if self.mode=="sheetToMusic":
			pass 

	def mousePressedMM(self,x,y):
		if self.mode=="musicMaking":
			pass 

	def mousePressed(self,x,y):
		self.mousePressedStart(x,y)
		self.mousePressedMTS(x,y)
		self.mousePressedSTM(x,y)
		self.mousePressedMM(x,y)

#### MouseReleased ####
	def mouseReleasedStart(self,x,y):
		if self.mode=="start":
			for btn in self.startBtnList:
				if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
					btn[4]=self.lightBlue
					self.mode=btn[5]

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
						if self.path!=None:
							self.mode="analyzing"
					else:
						self.mode="recording"

	def mouseReleasedSTM(self,x,y):
		if self.mode=="sheetToMusic":
			pass 

	def mouseReleasedMM(self,x,y):
		if self.mode=="musicMaking":
			pass

	def mouseReleasedBack(self,x,y):
		(width,height)=self.backBtnImage.get_size()
		if 10<=x<=width and 10<=y<=height:
			if self.mode=="recording":
				self.mode="musicToSheet"
			elif self.mode=="musicToSheet":
				self.mode="start"
			elif self.mode=="sheetToMusic":
				self.mode="start"
			elif self.mode=="musicMaking":
				self.mode="start"

	def mouseReleased(self,x,y):
		self.mouseReleasedStart(x,y)
		self.mouseReleasedMTS(x,y)
		self.mouseReleasedSTM(x,y)
		self.mouseReleasedMM(x,y)
		self.mouseReleasedBack(x,y)

#### MouseMotion ####
	def mouseMotionStart(self,x,y):
		if self.mode=="start":
			for btn in self.startBtnList:
				if self.within(btn[0],btn[1],btn[2],btn[3],x,y):
					btn[4]=self.darkBlue
				else:
					btn[4]=self.lightBlue

	def mouseMotionMTS(self,x,y):
		if self.mode=="musicToSheet":
			for btn in self.musicToSheetBtnList:
				if (x-btn[1])**2+(y-btn[2])**2 <= btn[3]**2:
					btn[0]=self.darkBlue 
				else:
					btn[0]=self.lightBlue

	def mouseMotionSTM(self,x,y):
		if self.mode=="sheetToMusic":
			pass 
			
	def mouseMotionMM(self,x,y):
		if self.mode=="musicMaking":
			pass 

	def mouseMotion(self, x, y):
		self.mouseMotionStart(x,y)
		self.mouseMotionMTS(x,y)
		self.mouseMotionSTM(x,y)
		self.mouseMotionMM(x,y)

### Key ###
	def keyPressed(self, keyCode, modifier):
		pass 
		
	def keyReleased(self, keyCode, modifier):
		pass
		
#### timerFried ####

	def timerFired(self, dt):
		if self.mode=="musicToSheet":
			self.mtsDelay+=1
   
		
###########################
#draw
##########################
	def displayText(self,screen,text,a,b,c,d,fontColor,font):
		#a,b=coordinates/ c=width, d=height
		myFont = font
		textSurface = myFont.render(text, True, fontColor)
		textRect1 = textSurface.get_rect()
		textRect1.center = (a + c//2, b + d//2)
		screen.blit(textSurface, textRect1)
		
	def displayTextAlignLeft(self,screen,text,a,b,fontColor,font):
		textSurface=font.render(text,True,fontColor)
		textRect1=textSurface.get_rect()
		screen.blit(textSurface,(a,b+5))
	   

### redraw ####
	def redrawStart(self,screen):
		if self.mode=="start":
			self.displayTextAlignLeft(screen,"Welcome to MusicReader",\
					self.width//8,self.height//5,self.black,self.regularFont)
			for btn in self.startBtnList:
				pygame.draw.rect(screen, btn[4], btn[:4])
			screen.blit(self.mtsIcon,(100,350))
			screen.blit(self.stmIcon,(326+51+100,350))
			screen.blit(self.mmIcon,(326*2+51*2+140,370))


	def redrawMTS(self,screen):
		if self.mode=="musicToSheet":
			for btn in self.musicToSheetBtnList:
				pygame.draw.circle(screen,btn[0],btn[1:3],btn[3])
				screen.blit(self.backBtnImage,(10,10))

	def redrawRecording(self,screen):
		if self.mode=="recording":
			screen.blit(self.backBtnImage,(10,10))

	def redrawAll(self, screen):
		self.redrawStart(screen)
		self.redrawMTS(screen)
		self.redrawRecording(screen)
		print(self.mode)

### RUN FUNCTION ###
### Copied from Hack112 group file 

	def isKeyPressed(self, key):
		#return whether a specific key is being held
		return self._keys.get(key, False)

	def __init__(self, width, height, fps=50, title="MusicReader"):
		self.width = width
		self.height = height
		self.fps = fps
		self.title = title

		pygame.init()
		

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
			self.redrawAll(screen)
			pygame.display.flip()

		pygame.quit()

def main():
	game = MusicReader(1280,720)
	game.run()

if __name__ == '__main__':
	main()
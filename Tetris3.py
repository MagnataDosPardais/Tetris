import pygame
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

Dimensions = (400, 600)
Window = pygame.display.set_mode(Dimensions)	#BLOCK = 25x25 // TELA = 300x500
Title = pygame.display.set_caption("TETRIS")
pygame.display.set_icon(pygame.image.load("Tetris.jpg"))

Models = {
	"S":[[[0,1,1],
		   [0,1,0],
		   [1,1,0]],

		 [[1,0,0],
		  [1,1,1],
		  [0,0,1]]],
	#----------------------------------------------
	#"s":[[[1,1,0],
	#	   [0,1,1],
	#	   [0,0,0]],
	#
	#	 [[1,0,0],
	#	  [1,1,0],
	#	  [0,1,0]]],
	#----------------------------------------------
	"L":[[[1,0,0],
		   [1,0,0],
		   [1,1,0]],

		 [[0,0,0],
		  [0,0,1],
		  [1,1,1]],

		 [[0,1,1],
		  [0,0,1],
		  [0,0,1]],

		 [[1,1,1],
		  [1,0,0],
		  [0,0,0]]],
	#----------------------------------------------
	"O":[[[1,1,0],
		   [1,1,0],
		   [0,0,0]]],
	#----------------------------------------------
	"T":[[[1,1,1],
		   [0,1,0],
		   [0,1,0]],

		 [[0,0,1],
		  [1,1,1],
		  [0,0,1]],

		 [[0,1,0],
		  [0,1,0],
		  [1,1,1]],

		 [[1,0,0],
		  [1,1,1],
		  [1,0,0]]],
	#----------------------------------------------
	"H":[[[1,0,1],
		   [1,1,1],
		   [1,0,1]],

		 [[1,1,1],
		  [0,1,0],
		  [1,1,1]]],
	#----------------------------------------------
	"I":[[[0,1,0],
		   [0,1,0],
		   [0,1,0]],

		 [[0,0,0],
		  [1,1,1],
		  [0,0,0]]],
	#----------------------------------------------
	"V":[[[1,1,1],
		   [0,0,1],
		   [0,0,1]],

		 [[0,0,1],
		  [0,0,1],
		  [1,1,1]],

		 [[1,0,0],
		  [1,0,0],
		  [1,1,1]],

		 [[1,1,1],
		  [1,0,0],
		  [1,0,0]]],
	#----------------------------------------------
	"Z":[[[1,1,0],
		   [0,1,0],
		   [0,1,1]],

		 [[0,0,1],
		  [1,1,1],
		  [1,0,0]]] ,
	#----------------------------------------------
	".":[[[0,0,0],
		   [0,1,0],
		   [0,0,0]]],
	#----------------------------------------------
	"+":[[[0,1,0],
		   [1,1,1],
		   [0,1,0]]]
	#----------------------------------------------
}

def gerateArray(lenX,lenY):
	makeArray = []
	for l in range(lenY):
		makeArray.append([" "]*lenX)
	return(makeArray)

class Board:
	def __init__(self,bArray,size=25):
		self.array = bArray
		self.lenArray = [len(self.array[0]),len(self.array)]
		self.size = size

	def DrawGrid(self,s,align,color=(20,20,20),bg=(0,0,0)):
		sx,sy = s
		sx = int((sx * self.size) + 1)
		sy = int((sy * self.size) + 1)
		if align.upper() == "CENTER":
			beginX = Dimensions[0]//2-(B.lenArray[0]//2*self.size)
			beginY = Dimensions[1]//2-(B.lenArray[1]//2*self.size)
		if align.upper() == "TOPLEFT":
			beginX = 0
			beginY = 0
		if align.upper() == "TOPCENTER":
			beginX = Dimensions[0]//2-(B.lenArray[0]//2*self.size)
			beginY = 0
		if align.upper() == "TOPRIGHT":
			beginX = Dimensions[0]-(B.lenArray[0]*self.size)
			beginY = 0
		if align.upper() == "BOTTOMLEFT":
			beginX = 0
			beginY = Dimensions[1]-((B.lenArray[1]-3)*self.size)
		if align.upper() == "BOTTOMCENTER":
			beginX = Dimensions[0]//2-(B.lenArray[0]//2*self.size)
			beginY = Dimensions[1]-((B.lenArray[1]-3)*self.size)
		if align.upper() == "BOTTOMRIGHT":
			beginX = Dimensions[0]-(B.lenArray[0]*self.size)
			beginY = Dimensions[1]-((B.lenArray[1]-3)*self.size)

		for x in range(beginX, sx+beginX, self.size):
			pygame.draw.line(Window, (color), (x, beginY), (x, sy+beginY))
		for y in range(beginY, sy+beginY, self.size):
			pygame.draw.line(Window, (color), (beginX, y), (sx+beginX, y))
		pygame.draw.rect(Window,colors[selectColor][2],[beginX,beginY-2,sx+2,2])
		pygame.draw.rect(Window,colors[selectColor][2],[beginX-2,beginY-2,2,sy+4])
		pygame.draw.rect(Window,colors[selectColor][2],[beginX+sx,beginY,2,sy])
		pygame.draw.rect(Window,colors[selectColor][2],[beginX,beginY+sy,sx+2,2])

	def includeShape(self,shape,direction,pos,align):
		adjustment = 0
		deslX = 0
		deslY = 0
		if (B.lenArray[0]%2 != 0):
			adjustment = 1
		for l in range(0,3):
			posY = pos[1]
			posY = posY + l
			for i in range(0,3):
				posX = pos[0]
				posX = posX + i + adjustment
				if Models[shape][direction][l][i] == 1:
					self.array[posY+deslY][posX+deslX] = shape

	def printPieces(self,tex):
		arrayX = self.lenArray[0]
		arrayY = self.lenArray[1]
		for l in range(0,arrayY):
			for i in range(0,arrayX):
				posX = (i+2) * self.size
				posY = (l+3) * self.size
				if self.array[l][i] != " ":
					for s in shapeList:
						if self.array[l][i] == s: colorShape = pygame.image.load(rf"Texturas/{tex}_{s}.jpg")
					Window.blit(colorShape,[posX,posY])

	def DrawHeader(self,size1=100,color=(255,255,255)):
		pygame.draw.rect(Window, color, [0,0,400,size1])

	def ValidateString(self):
		newLine = []
		point = 0
		for l in range(self.lenArray[1]-1,-1,-1):
			if not(" " in self.array[l]):
				for c in range(0, self.lenArray[0]):
					newLine.append(" ")
				self.array.pop(l)
				self.array.insert(0,newLine)
				newLine = []
				point = point + 1
				pygame.time.delay(200)
		return(point)

	def CheckLoose(self):
		state = True
		for l in range(0,2):
			for i in range(self.lenArray[0]):
				if self.array[l][i] != " ":
					state = False
					break
		return(state)

	def printHeader(self,icon="Star",text=None,size=12,begin=5,color=[0,0,0]):
		icon = pygame.image.load(rf"Images/{icon}.png")
		Window.blit(icon,(begin[0],begin[1]))
		FontSys = pygame.font.SysFont("Consolas", size)
		Font = FontSys.render(text,5,(color))
		Window.blit(Font,(begin[0]+30,begin[1]+7))


class Piece:
	def Draw(shape,direction,pos,tex):
		begin = [0,0]
		begin[0] = (pos[0]+(Dimensions[0]//2-(B.lenArray[0]//2*B.size))//B.size)*B.size
		begin[1] = (pos[1]+(Dimensions[1]//2-(B.lenArray[1]//2*B.size))//B.size)*B.size
		colorShape = pygame.image.load(rf"Texturas/{tex}_{shape}.jpg")
		for l in range(0,3):
			beginX, beginY = begin
			beginY = beginY + (l*B.size) + 1
			for i in range(0,3):
				beginX = begin[0] + 1
				beginX = beginX + (i*B.size)
				if Models[shape][direction][l][i] == 1:
					Window.blit(colorShape,[beginX,beginY])

	def sensorsRead(shape,direction,pos):
		sensorLeft = []
		sensorBottom = []
		sensorRight = []
		moveLeft = True
		moveBottom = True
		moveRight = True
		if shape == "S":
			if direction == 0:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]+24,pos[1]+1])
				sensorLeft[0] = Window.get_at([pos[0]+24,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]+24,pos[1]+49])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+51,pos[1]+26])
				sensorBottom[2] = Window.get_at([pos[0]+26,pos[1]+76])
				#Right:
				sensorRight = [0,0]
				sensorRight[0] = Window.get_at([pos[0]+51,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+24])
			if direction == 1:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+49])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+24,pos[1]+51])
				sensorBottom[1] = Window.get_at([pos[0]+49,pos[1]+51])
				sensorBottom[2] = Window.get_at([pos[0]+74,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+51])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+26])
				sensorRight[2] = Window.get_at([pos[0]+26,pos[1]+24])
		if shape == "L":
			if direction == 0:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0]
				sensorBottom[0] = Window.get_at([pos[0]+24,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+49,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+51,pos[1]+51])
				sensorRight[1] = Window.get_at([pos[0]+26,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+26,pos[1]+24])
			if direction == 1:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]+49,pos[1]+49])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+76])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+49])
			if direction == 2:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]+24,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]+49,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0]
				sensorBottom[0] = Window.get_at([pos[0]+49,pos[1]+26])
				sensorBottom[1] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+76,pos[1]+24])
			if direction == 3:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+51])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+26])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+26])
				#Right:
				sensorRight = [0,0]
				sensorRight[0] = Window.get_at([pos[0]+26,pos[1]+49])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+24])
		if shape == "O":
			#Left:
			sensorLeft = [0,0]
			sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
			sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
			#Bottom:
			sensorBottom = [0,0]
			sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+51])
			sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+51])
			#Right:
			sensorRight = [0,0]
			sensorRight[0] = Window.get_at([pos[0]+51,pos[1]+49])
			sensorRight[1] = Window.get_at([pos[0]+51,pos[1]+24])
		if shape == "T":
			if direction == 0:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]+24,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+24,pos[1]+26])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+76])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+26])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+51,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+51,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+76,pos[1]+24])
			if direction == 1:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]+49,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+24,pos[1]+51])
				sensorBottom[1] = Window.get_at([pos[0]+49,pos[1]+51])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+76,pos[1]+24])
			if direction == 2:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]+24,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]+24,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+76])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+51,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+51,pos[1]+24])
			if direction == 3:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+51])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+51])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+26,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+26,pos[1]+24])
		if shape == "H":
			if direction == 0:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+51])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+1])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+26])
				sensorRight[2] = Window.get_at([pos[0]+76,pos[1]+51])
			if direction == 1:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+24,pos[1]+26])
				sensorBottom[1] = Window.get_at([pos[0]+24,pos[1]+76])
				sensorBottom[2] = Window.get_at([pos[0]+49,pos[1]+76])
				sensorBottom[3] = Window.get_at([pos[0]+74,pos[1]+76])
				sensorBottom[4] = Window.get_at([pos[0]+51,pos[1]+26])
				#Right:
				sensorRight = [0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+1])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+51])
		if shape == "I":
			if direction == 0:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]+24,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]+24,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]+24,pos[1]+51])
				#Bottom:
				sensorBottom = [0]
				sensorBottom[0] = Window.get_at([pos[0]+26,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+51,pos[1]+24])
				sensorRight[1] = Window.get_at([pos[0]+51,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+51,pos[1]+74])
			if direction == 1:
				#Left:
				sensorLeft = [0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+26])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+24,pos[1]+51])
				sensorBottom[1] = Window.get_at([pos[0]+49,pos[1]+51])
				sensorBottom[2] = Window.get_at([pos[0]+74,pos[1]+51])
				#Right:
				sensorRight = [0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+26])
		if shape == "V":
			if direction == 0:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]+49,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+26])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+26])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+1])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+26])
				sensorRight[2] = Window.get_at([pos[0]+76,pos[1]+51])
			if direction == 1:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]+49,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]+49,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+76])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+24])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+76,pos[1]+74])
			if direction == 2:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+76])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+26,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+26,pos[1]+24])
			if direction == 3:
				#Left:
				sensorLeft = [0,0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
				sensorLeft[2] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+26])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+26])
				#Right:
				sensorRight = [0,0]
				sensorRight[0] = Window.get_at([pos[0]+26,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+24])
		if shape == "Z":
			if direction == 0:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+1,])
				sensorLeft[1] = Window.get_at([pos[0]+24,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+26])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+76])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+76])
				#Right:
				sensorRight = [0,0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+74])
				sensorRight[1] = Window.get_at([pos[0]+51,pos[1]+49])
				sensorRight[2] = Window.get_at([pos[0]+51,pos[1]+24])
			if direction == 1:
				#Left:
				sensorLeft = [0,0]
				sensorLeft[0] = Window.get_at([pos[0]-1,pos[1]+26])
				sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+51])
				#Bottom:
				sensorBottom = [0,0,0]
				sensorBottom[0] = Window.get_at([pos[0]+1,pos[1]+76])
				sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+51])
				sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+51])
				#Right:
				sensorRight = [0,0]
				sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+49])
				sensorRight[1] = Window.get_at([pos[0]+76,pos[1]+24])
		if shape == ".":
			#Left:
			sensorLeft = [0]
			sensorLeft[0] = Window.get_at([pos[0]+24,pos[1]+26])
			#Bottom:
			sensorBottom = [0]
			sensorBottom[0] = Window.get_at([pos[0]+26,pos[1]+51])
			#Right:
			sensorRight = [0]
			sensorRight[0] = Window.get_at([pos[0]+51,pos[1]+49])
		if shape == "+":
			#Left:
			sensorLeft = [0,0]
			sensorLeft[0] = Window.get_at([pos[0]+24,pos[1]+1])
			sensorLeft[1] = Window.get_at([pos[0]-1,pos[1]+26])
			#Bottom:
			sensorBottom = [0,0,0]
			sensorBottom[0] = Window.get_at([pos[0]+24,pos[1]+51])
			sensorBottom[1] = Window.get_at([pos[0]+26,pos[1]+76])
			sensorBottom[2] = Window.get_at([pos[0]+51,pos[1]+51])
			#Right:
			sensorRight = [0,0]
			sensorRight[0] = Window.get_at([pos[0]+76,pos[1]+49])
			sensorRight[1] = Window.get_at([pos[0]+51,pos[1]+24])
		#CheckMove:
		for sl in sensorLeft:
			if sl != colors[selectColor][0]:
				moveLeft = False
				break
			else:
				moveLeft = True
		for sb in sensorBottom:
			if sb != colors[selectColor][0]:
				moveBottom = False
				break
			else:
				moveBottom = True
		for sr in sensorRight:
			if sr != colors[selectColor][0]:
				moveRight = False
				break
			else:
				moveRight = True
		#Return Bool:
		return [moveLeft,moveBottom,moveRight]


#Coordinate:
x = 4
y = 0
#Color:
colors = [[(0,0,0),(20,20,20),(255,255,255)],
			 [(50,50,50),(70,70,70),(255,255,255)],
			 [(150,150,150),(130,130,130),(0,0,0)],
			 [(255,255,255),(200,200,200),(0,0,0)]]
#Objects:
a = gerateArray(12,18)
B = Board(a,25)
#Execute:
menu = True
animaIntro = True
animaArrow = [0,False]
menuSelect = 0
run = False
tutorial = [False,0]
options = [False,0]
quitGame = False
defeat = False
#Images:
menuImage = pygame.image.load(r"Intro/Intro11.png")
Cel_UmOitavo_de_Bytes = pygame.image.load(r"Intro/LoseWithStyle.jpg")
texture = ["Plain","Adobe","Brick","Exhausted","Line","Mine","Neon"]
selectTexture = 0
selectColor = 0
#Sounds:
moveSound = pygame.mixer.Sound(r"Intro/Tap.mp3")
slapSound = pygame.mixer.Sound(r"Intro/Slap.mp3")
#Markers:
score = 0
turns = 0
hold = "---"
auxHold = ""
#Piece:
shapeList = ["S", "L", "O", "T", "H", "I", "V", "Z", ".", "+"]
pDir = 0
P = [random.choice(shapeList),pDir,[x,y]]
#ColiderLists:
freeLeft = True
freeFall = True
freeRight = True
#Clock:
clock = pygame.time.Clock()
gameFPS = 6
auxGameFPS = False
speed = 3
auxSpeed = 0
dawnPiece = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

	if menu:
		Window.fill([10,10,15])
		if animaIntro:
			pygame.time.delay(1000)
			for s in range(1,12):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()
				Key = pygame.key.get_pressed()
				if Key[ord("q")]:
					break
				Window.fill([10,10,15])
				sprite = pygame.image.load(rf"Intro/Intro{s}.png")
				Window.blit(sprite,(5,10))
				if s == 11:
					slapSound.play()
				else:
					moveSound.play()
				pygame.time.delay(420)
				pygame.display.update()
			animaIntro = False
			pygame.time.delay(600)

		Window.blit(menuImage,(5,10))
		Key = pygame.key.get_pressed()
		if Key[ord("d")] or Key[ord("a")]:
			menu = False
			B.array = gerateArray(12,18)
			score = 0
			turns = 0
			hold = "---"
			auxHold = ""
			pygame.time.delay(200)
		if Key[ord("w")]:
			menuSelect = menuSelect - 1
			animaArrow[1] = 0
			if menuSelect < 0:
				menuSelect = 3
			pygame.time.delay(100)
		if Key[ord("s")]:
			menuSelect = menuSelect + 1
			animaArrow[1] = 0
			if menuSelect > 3:
				menuSelect = 0
			pygame.time.delay(100)

		FontSys = pygame.font.SysFont("VCR OSD Mono",28)
		Font = FontSys.render("Passar raiva",5,(255,255,255))
		Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),300))
		if menuSelect == 0:
			B.printHeader("Arrow_Red","",1,[Dimensions[0]//2-(Font.get_width()//2)-30-animaArrow[1],300])
			run = True
			tutorial[0] = False
			quitGame = False
			options[0] = False
		Font = FontSys.render("Opções",5,(255,255,255))
		Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),350))
		if menuSelect == 1:
			B.printHeader("Arrow_Red","",1,[Dimensions[0]//2-(Font.get_width()//2)-30-animaArrow[1],350])
			run = False
			tutorial[0] = False
			quitGame = False
			options[0] = True
		Font = FontSys.render("Tutorial",5,(255,255,255))
		Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),400))
		if menuSelect == 2:
			B.printHeader("Arrow_Red","",1,[Dimensions[0]//2-(Font.get_width()//2)-30-animaArrow[1],400])
			run = False
			tutorial[0] = True
			quitGame = False
			options[0] = False
		Font = FontSys.render("Sair",5,(255,255,255))
		Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),450))
		if menuSelect == 3:
			B.printHeader("Arrow_Red","",1,[Dimensions[0]//2-(Font.get_width()//2)-30-animaArrow[1],450])
			run = False
			tutorial[0] = False
			quitGame = True
			options[0] = False

		if not(animaArrow[0]):
			animaArrow[1] = animaArrow[1] + 1
			pygame.time.delay(20)
			if animaArrow[1] >= 10:
				animaArrow[0] = True
		if animaArrow[0]:
			animaArrow[1] = animaArrow[1] - 1
			pygame.time.delay(20)
			if animaArrow[1] <= 0:
				animaArrow[0] = False
		pygame.display.update()

	if run and not(menu):
		#Keyboard:
		print(gameFPS)
		print(speed)
		Key = pygame.key.get_pressed()
		if Key[ord("j")]:
			auxGameFPS = True
			freeRight = False
			freeLeft = False
		if Key[ord("s")]:
			gameFPS = 50
		else:
			if auxGameFPS:
				gameFPS = 1500
			else:
				gameFPS = 8
		if Key[ord("h")]:
			if hold == "---":
				hold = P[0]
				shapeList.remove(P[0])
				P = [random.choice(shapeList),pDir,[x,y]]
				shapeList = ["S", "L", "O", "T", "H", "I", "V", "Z", ".", "+"]
			else:
				auxHold = hold
				hold = P[0]
				P[0] = auxHold
			pDir = 0
			x = 4
			y = 0
		if Key[ord("d")] and freeRight:
			x += 1
		if Key[ord("a")] and freeLeft:
			x -= 1
		if Key[ord("w")]:
			if not(P[0]=="I" and pDir==0 and (x<=-1 or x>=B.lenArray[0]-2)) and\
				not(P[0]=="L" and pDir==0 and (x>=B.lenArray[0]-2)) and\
				not(P[0]=="L" and pDir==2 and (x<=-1)) and\
				not(P[0]=="L" and pDir==3 and (x>=B.lenArray[1]-2)):
				pDir = pDir + 1
			if P[0] == "S" and pDir > 1: pDir = 0
			if P[0] == "L" and pDir > 3: pDir = 0
			if P[0] == "O" and pDir > 0: pDir = 0
			if P[0] == "T" and pDir > 3: pDir = 0
			if P[0] == "H" and pDir > 1: pDir = 0
			if P[0] == "I" and pDir > 1: pDir = 0
			if P[0] == "V" and pDir > 3: pDir = 0
			if P[0] == "Z" and pDir > 1: pDir = 0
			if P[0] == "." and pDir > 0: pDir = 0
			if P[0] == "+" and pDir > 0: pDir = 0
		#Verify defeat:
		run = B.CheckLoose()
		defeat = not(run)
		#Run&Colide:
		if dawnPiece:
			if not(freeFall):
				#Stamp piece in Array
				B.includeShape(P[0],P[1],P[2],"CENTER")
				pDir = 0
				x = 4
				y = 0
				P = [random.choice(shapeList),pDir,[x,y]]
				turns = turns + 1
				auxGameFPS = False
				pygame.time.delay(1000)
			else:
				y += 1
		P[1] = pDir
		P[2] = [x,y]
		#fill BG:
		Window.fill(colors[selectColor][0])
		#Update:
		B.printPieces(texture[selectTexture])
		#Draw Currently Piece:
		Piece.Draw(P[0],P[1],P[2],texture[selectTexture])
		#Grid:
		B.DrawGrid(B.lenArray,"CENTER",colors[selectColor][1],colors[selectColor][0])
		#Read colors:
		freeLeft,freeFall,freeRight = Piece.sensorsRead(P[0],P[1],[P[2][0]*25+50,P[2][1]*25+75])
		#CheckLines:
		score = score + B.ValidateString()
		print(score)
		#Header/Footer:
		B.DrawHeader(55)
		B.printHeader("Star",f"Score:{score}",16,[0,0])
		B.printHeader("Piece",f"Turn:{turns}",16,[0,25])
		B.printHeader("Hand",f"Hold:{hold}",16,[150,0])
		#Update:
		clock.tick(gameFPS)
		auxSpeed = auxSpeed + 1
		if auxSpeed == speed:
			dawnPiece = True
			auxSpeed = 0
		else:
			dawnPiece = False
		pygame.display.update()

	if defeat and not(menu):
		Window.fill([0,0,0])
		Window.blit(Cel_UmOitavo_de_Bytes,[0,0])
		Key = pygame.key.get_pressed()
		if Key[ord("q")]:
			menu = True
			defeat = False
			score = 0
			turns = 0
			hold = "---"
			auxHold = ""
			pygame.time.delay(200)
		FontSys = pygame.font.SysFont("VCR OSD Mono",28)
		Font = FontSys.render(f"Score:{score}",5,(255,255,255))
		Window.blit(Font,(5,435))
		Font = FontSys.render(f"Turns:{turns}",5,(255,255,255))
		Window.blit(Font,(5,470))

	if options[0] and not(menu):
		Window.fill([10,10,15])
		if selectColor == 0:
			statusBG = "Muito-escuro"
		if selectColor == 1:
			statusBG = "Escuro"
		if selectColor == 2:
			statusBG = "Claro"
		if selectColor == 3:
			statusBG = "Psicopata"
		
		Key = pygame.key.get_pressed()
		if Key[ord("q")]:
			options[0] = False
			menu = True
		if Key[ord("w")]:
			options[1] = options[1] - 1
			if options[1] < 0:
				options[1] = 1
			pygame.time.delay(150)
		if Key[ord("s")]:
			options[1] = options[1] + 1
			if options[1] > 1:
				options[1] = 0
			pygame.time.delay(150)
		if Key[ord("a")]:
			if options[1] == 0:
				selectTexture = selectTexture - 1
			if options[1] == 1:
				selectColor = selectColor - 1
			pygame.time.delay(150)
		if Key[ord("d")]:
			if options[1] == 0:
				selectTexture = selectTexture + 1
			if options[1] == 1:
				selectColor = selectColor + 1
			pygame.time.delay(150)

		if selectTexture > len(texture)-1:
			selectTexture = 0
		elif selectTexture < 0:
			selectTexture = len(texture)-1

		if selectColor > len(colors)-1:
			selectColor = 0
		elif selectColor < 0:
			selectColor = len(colors)-1

		FontSys = pygame.font.SysFont("VCR OSD Mono",18)
		Font = FontSys.render("<--Q",5,(255,255,255))
		Window.blit(Font,(5,5))
		
		FontSys = pygame.font.SysFont("VCR OSD Mono",36)
		Font = FontSys.render("Opções",5,(255,255,255))
		Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),25))
		
		FontSys = pygame.font.SysFont("VCR OSD Mono",18)
		Font = FontSys.render(f"Skin:{texture[selectTexture]}",5,(255,255,255))
		Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),200))
		if options[1] == 0:
			if selectTexture != 3:
				B.printHeader("Arrow_Red","",1,[265+animaArrow[1],195+(options[1]*40)])
				B.printHeader("Arrow_Red_I","",1,[110-animaArrow[1],195+(options[1]*40)])
			else:
				B.printHeader("Arrow_Red","",1,[295+animaArrow[1],195+(options[1]*40)])
				B.printHeader("Arrow_Red_I","",1,[80-animaArrow[1],195+(options[1]*40)])
		if options[1] == 1:
			if selectColor == 0:
				statusBG = "Muito-escuro"
				B.printHeader("Arrow_Red","",1,[335+animaArrow[1],195+(options[1]*40)])
				B.printHeader("Arrow_Red_I","",1,[40-animaArrow[1],195+(options[1]*40)])
			if selectColor == 1:
				statusBG = "Escuro"
				B.printHeader("Arrow_Red","",1,[300+animaArrow[1],195+(options[1]*40)])
				B.printHeader("Arrow_Red_I","",1,[75-animaArrow[1],195+(options[1]*40)])
			if selectColor == 2:
				statusBG = "Claro"
				B.printHeader("Arrow_Red","",1,[295+animaArrow[1],195+(options[1]*40)])
				B.printHeader("Arrow_Red_I","",1,[80-animaArrow[1],195+(options[1]*40)])
			if selectColor == 3:
				statusBG = "Psicopata"
				B.printHeader("Arrow_Red","",1,[330+animaArrow[1],195+(options[1]*40)])
				B.printHeader("Arrow_Red_I","",1,[50-animaArrow[1],195+(options[1]*40)])
		Font = FontSys.render(f"Background:{statusBG}",5,(255,255,255))
		Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),240))

		if not(animaArrow[0]):
			animaArrow[1] = animaArrow[1] + 1
			pygame.time.delay(20)
			if animaArrow[1] >= 10:
				animaArrow[0] = True
		if animaArrow[0]:
			animaArrow[1] = animaArrow[1] - 1
			pygame.time.delay(20)
			if animaArrow[1] <= 0:
				animaArrow[0] = False

	if tutorial[0] and not(menu):
		Window.fill([10,10,15])
		if tutorial[1] == 0:
			for t in range(10,180):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()
				Key = pygame.key.get_pressed()
				if Key[ord("q")]:
					tutorial[0] = False
					menu = True
					break
				if Key[ord("d")]:
					tutorial[1] = tutorial[1] + 1
					pygame.time.delay(150)
					break
				
				Window.fill([10,10,15])
				FontSys = pygame.font.SysFont("VCR OSD Mono",18)
				Font = FontSys.render("<--Q",5,(255,255,255))
				Window.blit(Font,(5,5))
				FontSys = pygame.font.SysFont("VCR OSD Mono",36)
				Font = FontSys.render("Mover",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),25))
				FontSys = pygame.font.SysFont("VCR OSD Mono",18)
				Font = FontSys.render("Teclas de seta.",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),100))
				if t//10 <= 6:
					Font = FontSys.render("Esquerda = 'A'",5,(255,255,255))
					Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),125))
					pygame.time.delay(30)
				if t//10 > 6 and t//10 <= 9:
					Font = FontSys.render("Direita = 'D'",5,(255,255,255))
					Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),125))
					pygame.time.delay(30)
				if t//10 == 10 or t//10 == 11:
					Font = FontSys.render("Virar = 'W'",5,(255,255,255))
					Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),125))
					pygame.time.delay(30)
				if t//10 >= 12:
					Font = FontSys.render("Descer rápido = 'S'",5,(255,255,255))
					Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),125))
				isnSlide = pygame.image.load(rf"Tutorial/Move{t//10}.png")
				Window.blit(isnSlide,(Dimensions[0]//2-(isnSlide.get_width()//2),150))
				
				B.printHeader("Arrow_Red","",1,[350+animaArrow[1],340])
				if not(animaArrow[0]):
					animaArrow[1] = animaArrow[1] + 1
					pygame.time.delay(20)
					if animaArrow[1] >= 10:
						animaArrow[0] = True
				if animaArrow[0]:
					animaArrow[1] = animaArrow[1] - 1
					pygame.time.delay(20)
					if animaArrow[1] <= 0:
						animaArrow[0] = False

				if not(t//10 >= 12):
					pygame.time.delay(12)
				pygame.display.update()
		
		if tutorial[1] == 1:
			for t in range(10,80):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()
				Key = pygame.key.get_pressed()
				if Key[ord("q")]:
					tutorial[0] = False
					menu = True
					break
				if Key[ord("d")]:
					tutorial[1] = tutorial[1] + 1
					pygame.time.delay(150)
					break
				if Key[ord("a")]:
					tutorial[1] = tutorial[1] - 1
					pygame.time.delay(150)
					break
				Window.fill([10,10,15])
				FontSys = pygame.font.SysFont("VCR OSD Mono",18)
				Font = FontSys.render("<--Q",5,(255,255,255))
				Window.blit(Font,(5,5))
				FontSys = pygame.font.SysFont("VCR OSD Mono",36)
				Font = FontSys.render("Segurar",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),25))
				FontSys = pygame.font.SysFont("VCR OSD Mono",18)
				Font = FontSys.render("Guarde a peça para depois",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),100))
				Font = FontSys.render("Hold = 'H'",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),125))
				isnSlide = pygame.image.load(rf"Tutorial/Keep{t//10}.png")
				Window.blit(isnSlide,(Dimensions[0]//2-(isnSlide.get_width()//2),150))

				B.printHeader("Arrow_Red","",1,[350+animaArrow[1],340])
				B.printHeader("Arrow_Red_I","",1,[25-animaArrow[1],340])
				if not(animaArrow[0]):
					animaArrow[1] = animaArrow[1] + 1
					pygame.time.delay(20)
					if animaArrow[1] >= 10:
						animaArrow[0] = True
				if animaArrow[0]:
					animaArrow[1] = animaArrow[1] - 1
					pygame.time.delay(20)
					if animaArrow[1] <= 0:
						animaArrow[0] = False
				pygame.time.delay(42)
				pygame.display.update()
		pygame.display.update()

		if tutorial[1] == 2:
			for t in range(10,100):
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()
				Key = pygame.key.get_pressed()
				if Key[ord("q")]:
					tutorial[0] = False
					menu = True
					break
				if Key[ord("a")]:
					tutorial[1] = tutorial[1] - 1
					pygame.time.delay(150)
					break
				Window.fill([10,10,15])
				FontSys = pygame.font.SysFont("VCR OSD Mono",18)
				Font = FontSys.render("<--Q",5,(255,255,255))
				Window.blit(Font,(5,5))
				FontSys = pygame.font.SysFont("VCR OSD Mono",36)
				Font = FontSys.render("Pontuar",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),25))
				FontSys = pygame.font.SysFont("VCR OSD Mono",18)
				Font = FontSys.render("Complete uma linha para pontuar!",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),100))
				Font = FontSys.render("(1 ponto por linha)",5,(255,255,255))
				Window.blit(Font,(Dimensions[0]//2-(Font.get_width()//2),125))
				isnSlide = pygame.image.load(rf"Tutorial/Ponto{t//10}.png")
				Window.blit(isnSlide,(Dimensions[0]//2-(isnSlide.get_width()//2),150))

				B.printHeader("Arrow_Red_I","",1,[25-animaArrow[1],340])
				if not(animaArrow[0]):
					animaArrow[1] = animaArrow[1] + 1
					pygame.time.delay(20)
					if animaArrow[1] >= 10:
						animaArrow[0] = True
				if animaArrow[0]:
					animaArrow[1] = animaArrow[1] - 1
					pygame.time.delay(20)
					if animaArrow[1] <= 0:
						animaArrow[0] = False

				pygame.time.delay(42)
				pygame.display.update()

	if quitGame and not(menu):
		pygame.quit()
		exit()
	
	pygame.display.update()
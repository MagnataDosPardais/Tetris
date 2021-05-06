import pygame
import random

Dimensions = ((400, 600))
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
}

class Board:
	def DrawGrid(s=[16,24],size=25,begin=(0,0),color=(20,20,20)):
		sx,sy = s
		sx = int((sx * size) + 1)
		sy = int((sy * size) + 1)
		beginX, beginY = begin
		for x in range(beginX, sx+beginX, size):
			pygame.draw.line(Window, (color), (x, beginY), (x, sy+beginY))
		for y in range(beginY, sy+beginY, size):
			pygame.draw.line(Window, (color), (beginX, y), (sx+beginX, y))
		pygame.draw.rect(Window,(0,0,0),[beginX+sx,beginY,2,sy])
		pygame.draw.rect(Window,(0,0,0),[beginX,beginY+sy,sx,2])

	def DrawHeader(size=100,color=(255,255,255)):
		pygame.draw.rect(Window, color, [0,0,400,size])

	def Stamp(shape,direction,pos):
		global boardArray
		global Models
		shapeArray = Models[shape][direction]
		posX, posY = pos
		for l in range(0,3):
			posY = pos[1]
			posY = posY + l
			for i in range(0,3):
				posX = pos[0]
				posX = posX + i
				if Models[shape][direction][l][i] == 1:
					boardArray[posY][posX] = shape

	def Rearrange(array):
		arrayX = len(array[0])
		arrayY = len(array)
		for l in range(0,arrayY):
			for i in range(0,arrayX):
				posX = (i+2) * 25
				posY = (l+3) * 25
				if array[l][i] == "S":
					colorShape = (255,255,0)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "L":
					colorShape = (0,255,0)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "O":
					colorShape = (0,0,255)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "T":
					colorShape = (255,0,0)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "H":
					colorShape = (255,0,255)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "I":
					colorShape = (0,255,255)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "V":
					colorShape = (255,55,0)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "Z":
					colorShape = (20,0,110)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == ".":
					colorShape = (45,25,0)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])
				if array[l][i] == "+":
					colorShape = (80,80,80)
					pygame.draw.rect(Window, colorShape, [posX,posY,25,25])



class Pieces:
	def Raffle():
		shapes = ["S", "L", "O", "T", "H", "I", "V", "Z", ".", "+"]
		return(shapes[random.randint(0,9)])

	def Draw(shape, direction, begin):
		if shape == "S": colorShape = (255,255,0)
		if shape == "L": colorShape = (0,255,0)
		if shape == "O": colorShape = (0,0,255)
		if shape == "T": colorShape = (255,0,0)
		if shape == "H": colorShape = (255,0,255)
		if shape == "I": colorShape = (0,255,255)
		if shape == "V": colorShape = (255,55,0)
		if shape == "Z": colorShape = (20,0,110)
		if shape == ".": colorShape = (45,25,0)
		if shape == "+": colorShape = (80,80,80)
		for l in range(0,3):
			beginX, beginY = begin
			beginY = beginY + (l*25) + 1
			#print(f"Line[{l}]: {Models[shape][direction][l]}")
			for i in range(0,3):
				#print(f"Char[{i}]: {Models[shape][direction][l][i]}")
				beginX = begin[0] + 1
				beginX = beginX + (i*25)
				#print(beginX)
				if Models[shape][direction][l][i] == 1:
					pygame.draw.rect(Window, colorShape, [beginX,beginY,25,25])

	def AdjustCollision(shape,direction,mousePos):
		mouseX, mouseY = mousePos
		if shape == "S" or shape == "Z" or shape == "+" or shape == "T" or shape == "H" or shape == "V":
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
			if mouseY > 500: mouseY = 500
			if mouseY < 75: mouseY = 75
		if shape == "L" and direction == 0:
			if mouseX > 300: mouseX = 300
			if mouseX < 50: mouseX = 50
			if mouseY > 500: mouseY = 500
			if mouseY < 75: mouseY = 75
		if shape == "L" and direction == 1:
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
			if mouseY > 500: mouseY = 500
			if mouseY < 50: mouseY = 50
		if shape == "L" and direction == 2:
			if mouseX > 275: mouseX = 275
			if mouseX < 25: mouseX = 25
			if mouseY > 500: mouseY = 500
			if mouseY < 75: mouseY = 75
		if shape == "L" and direction == 3:
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
			if mouseY > 525: mouseY = 525
			if mouseY < 75: mouseY = 75
		if shape == "I" and direction == 0:
			if mouseX > 300: mouseX = 300
			if mouseX < 25: mouseX = 25
			if mouseY > 500: mouseY = 500
			if mouseY < 75: mouseY = 75
		if shape == "I" and direction == 1:
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
			if mouseY > 525: mouseY = 525
			if mouseY < 50: mouseY = 50
		if shape == ".":
			if mouseX > 300: mouseX = 300
			if mouseX < 25: mouseX = 25
			if mouseY > 525: mouseY = 525
			if mouseY < 50: mouseY = 50
		if shape == "O":
			if mouseX > 300: mouseX = 300
			if mouseX < 50: mouseX = 50
			if mouseY > 525: mouseY = 525
			if mouseY < 75: mouseY = 75
		return (mouseX//25,mouseY//25)



modeloAtual = Pieces.Raffle()
dirAtual = 0
boardArray = [
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""],
["","","","","","","","","","","",""]]

while True:
	Window.fill((0,0,0))
	
	Mouse = pygame.mouse.get_pos() 
	MouseXA, MouseYA = Pieces.AdjustCollision(modeloAtual,dirAtual,Mouse)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.MOUSEBUTTONUP:
			dirAtual = 0
			modeloAtual = Pieces.Raffle()
			#print(modeloAtual)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				dirAtual = dirAtual + 1
				if modeloAtual == "S" and dirAtual > 1: dirAtual = 0
				if modeloAtual == "L" and dirAtual > 3: dirAtual = 0
				if modeloAtual == "O" and dirAtual > 0: dirAtual = 0
				if modeloAtual == "T" and dirAtual > 3: dirAtual = 0
				if modeloAtual == "H" and dirAtual > 1: dirAtual = 0
				if modeloAtual == "I" and dirAtual > 1: dirAtual = 0
				if modeloAtual == "V" and dirAtual > 3: dirAtual = 0
				if modeloAtual == "Z" and dirAtual > 1: dirAtual = 0
				if modeloAtual == "." and dirAtual > 0: dirAtual = 0
				if modeloAtual == "+" and dirAtual > 0: dirAtual = 0
			if event.key == pygame.K_m:
				Board.Stamp(modeloAtual,dirAtual,[MouseXA-2,MouseYA-3])

	Board.DrawGrid([12,20],25,[50,75])
	Board.DrawHeader(50,(50,50,50))
	Pieces.Draw(modeloAtual, dirAtual,[MouseXA*25,MouseYA*25])
	Board.Rearrange(boardArray)
	pygame.display.update()


# quadro = 
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","_","_","_","_","_","_"]
	# ["_","S","S","_","_","_","_"]
	# ["_","S","O","O","_","_","_"]
	#if not("_" in quadro[0]):
	#	pass

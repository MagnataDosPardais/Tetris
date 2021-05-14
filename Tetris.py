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
#----------------------------------------------
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
		posX, posY = pos
		#print(f"Coo={pos}, Format={shape}")
		for l in range(0,3):
			posY = pos[1]
			posY = posY + l
			for i in range(0,3):
				posX = pos[0]
				posX = posX + i
				#print(f"X={posX}, Y={posY}")
				if Models[shape][direction][l][i] == 1:
					boardArray[posY][posX] = shape
					#print(boardArray[posY][posX])
		for nl in range(0,20):
			print(boardArray[nl])


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

	def ValidateString(array):
		global boardArray
		newLine = []
		arrayX = len(array[0])
		arrayY = len(array)
		#print(newLine)
		#print(f"X={arrayX} / Y={arrayY}")
		for l in range(arrayY-1,-1,-1):		
			if not(" " in array[l]):
				for c in range(0, arrayX):
					newLine.append(" ")
				print(f"C=Line:[{l}]")
				array.pop(l)
				array.insert(0,newLine)
				boardArray = array
				newLine = []
				pygame.time.delay(200)
		for ln in range(0,20):
			print(boardArray[ln])
		print("---------------------------------------------")


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
			#print(shape, direction)
			for i in range(0,3):
				#print(f"Char[{i}]: {Models[shape][direction][l][i]}")
				beginX = begin[0] + 1
				beginX = beginX + (i*25)
				#print(beginX)
				if Models[shape][direction][l][i] == 1:
					pygame.draw.rect(Window, colorShape, [beginX,beginY,25,25])

	def AdjustCollision(shape,direction,mousePos,array):
		global dirAtual
		global boardArray
		mouseX, mouseY = mousePos
		arrayX = len(array[0])
		arrayY = len(array)
		listGround = []
		limitPieceB = []
		limitPieceL = []
		limitPieceR = []
		newShape = [False,shape]

#------------------------------------------------------------------------------------
		for i in range(0,arrayX):
			for l in range(0,arrayY):
				if array[l][i] != " ":
					listGround.append((l)*25)
					break
				if l == arrayY-1 and (array[l][i] == " "):
					listGround.append((arrayY)*25)
		print(f"Col={listGround}")

		for v in range(0,3):
			for h in range(2,-1,-1):
				if Models[shape][direction][h][v]:
					limitPieceB.append(h)
					break
				if h == 0 and (Models[shape][direction][h][v] == 0):
					limitPieceB.append(-1)
		print(f"Base={limitPieceB}")

		for h in range(2,-1,-1):
			for v in range(0,3):
				if Models[shape][direction][h][v]:
					limitPieceL.append(v)
					break
				if v == 2 and (Models[shape][direction][h][v] == 0):
					limitPieceL.append(-1)
		print(f"Esq={limitPieceL}")

		for h in range(2,-1,-1):
			for v in range(2,-1,-1):
				if Models[shape][direction][h][v]:
					limitPieceR.append(v*-1+2)
					break
				if v == 0 and (Models[shape][direction][h][v] == 0):
					limitPieceR.append(-1)
		print(f"Dir={limitPieceR}")
#------------------------------------------------------------------------------------		

		if shape == "S" or shape == "Z" or shape == "+" or shape == "T" or shape == "H" or shape == "V":
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
		elif shape == "L" and direction == 0:
			if mouseX > 300: mouseX = 300
			if mouseX < 50: mouseX = 50
		elif shape == "L" and direction == 1:
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
		elif shape == "L" and direction == 2:
			if mouseX > 275: mouseX = 275
			if mouseX < 25: mouseX = 25
		elif shape == "L" and direction == 3:
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
		elif shape == "I" and direction == 0:
			if mouseX > 300: mouseX = 300
			if mouseX < 25: mouseX = 25
		elif shape == "I" and direction == 1:
			if mouseX > 275: mouseX = 275
			if mouseX < 50: mouseX = 50
		elif shape == ".":
			if mouseX > 300: mouseX = 300
			if mouseX < 25: mouseX = 25
		elif shape == "O":
			if mouseX > 300: mouseX = 300
			if mouseX < 50: mouseX = 50


		print(shape)
		print(f"Y={mouseY}")
		print(f"X={mouseX}")
		for c in range(0,3):
			#print(f"index={((mouseX//25)-2)+c}")
			if(limitPieceB[c] != -1):
				#print(f"limIndex[{((mouseX//25)-2)+c}]={listGround[((mouseX//25)-2)+c]-(limitPieceB[c]*25)}")
				#print(f"SP{listGround[((mouseX//25)-2)+c]}/IP={mouseY+(limitPieceB[c]*25)}")
				if listGround[((mouseX//25)-2)+c] <= mouseY+(limitPieceB[c]*25)-75:
					Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
					mouseX = 150
					mouseY = 75
					newShape[0] = True
					dirAtual = 0
					#print("A")
					pass

		if newShape[0] == True: newShape[1] = Pieces.Raffle()
		return (mouseX,mouseY,newShape[1])

		# #if shape == "S" or shape == "Z" or shape == "+" or shape == "T" or shape == "H" or shape == "V":
		# 	if mouseX > 275: mouseX = 275
		# 	if mouseX < 50: mouseX = 50
		# 	if mouseY > 500:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 75
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 75: mouseY = 75
		# #elif shape == "L" and direction == 0:
		# 	if mouseX > 300: mouseX = 300
		# 	if mouseX < 50: mouseX = 50
		# 	if mouseY > 500:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 75
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 75: mouseY = 75
		# #elif shape == "L" and direction == 1:
		# 	if mouseX > 275: mouseX = 275
		# 	if mouseX < 50: mouseX = 50
		# 	if mouseY > 500:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 50
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 50: mouseY = 50
		# #elif shape == "L" and direction == 2:
		# 	if mouseX > 275: mouseX = 275
		# 	if mouseX < 25: mouseX = 25
		# 	if mouseY > 500:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 75
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 75: mouseY = 75
		# #elif shape == "L" and direction == 3:
		# 	if mouseX > 275: mouseX = 275
		# 	if mouseX < 50: mouseX = 50
		# 	if mouseY > 525: 
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 75
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 75: mouseY = 75
		# #elif shape == "I" and direction == 0:
		# 	if mouseX > 300: mouseX = 300
		# 	if mouseX < 25: mouseX = 25
		# 	if mouseY > 500:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 75
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 75: mouseY = 75
		# #elif shape == "I" and direction == 1:
		# 	if mouseX > 275: mouseX = 275
		# 	if mouseX < 50: mouseX = 50
		# 	if mouseY > 525:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 50
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 50: mouseY = 50
		# #elif shape == ".":
		# 	if mouseX > 325: mouseX = 325
		# 	if mouseX < 50: mouseX = 50
		# 	if mouseY > 525:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 50
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 50: mouseY = 50
		# #elif shape == "O":
		# 	if mouseX > 300: mouseX = 300
		# 	if mouseX < 50: mouseX = 50
		# 	if mouseY > 525:
		# 		Board.Stamp(modeloAtual,dirAtual,[(mouseX//25-2),(mouseY//25-4)])
		# 		mouseX = 150
		# 		mouseY = 75
		# 		newShape[0] = True
		# 		dirAtual = 0
		# 	if mouseY < 75: mouseY = 75



modeloAtual = Pieces.Raffle()
dirAtual = 0
boardArray = [
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "],
[" "," "," "," "," "," "," "," "," "," "," "," "]]
begX = 150
begY = 75
deltaV = 0
clock = pygame.time.Clock()

while True:
	Window.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		#if event.type == pygame.MOUSEBUTTONUP:
		#	dirAtual = 0
		#	modeloAtual = Pieces.Raffle()
		#	print(modeloAtual)
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
			if event.key == pygame.K_a and event.key == pygame.K_d:
				pass
			elif event.key == pygame.K_a:
				begX = begX - 25
			elif event.key == pygame.K_d:
				begX = begX + 25

	Key = pygame.key.get_pressed()
	if Key[ord("s")]:
		deltaV = 20
	else:
		deltaV = 6
	if Key[ord("a")] and not(Key[ord("d")]):
		begX = begX - 25
		pygame.time.delay(90)
	if Key[ord("d")] and not(Key[ord("a")]):
		begX = begX + 25
		pygame.time.delay(90)

	begX,begY,modeloAtual = Pieces.AdjustCollision(modeloAtual,dirAtual,[begX,begY],boardArray)
	Board.ValidateString(boardArray)
	Board.Rearrange(boardArray)
	Pieces.Draw(modeloAtual,dirAtual,[begX,begY])
	Board.DrawGrid([12,20],25,[50,75])
	Board.DrawHeader(50,(50,50,50))
	clock.tick(deltaV)
	begY = begY + 25
	pygame.display.update()

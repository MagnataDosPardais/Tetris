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

modeloAtual = "S"

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

	def Stamp():
		pass

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

	def Rotate(direction=0)



while True:
	Window.fill((0,0,0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.MOUSEBUTTONUP:
			modeloAtual = Pieces.Raffle()
			print(modeloAtual)

	Mouse = pygame.mouse.get_pos()
	MouseX, MouseY = Mouse
	Board.DrawGrid([14,20],25,[25,75],(255,0,0))
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
	
	Board.DrawHeader(50,(50,50,50))
	Pieces.Draw(modeloAtual, 0,[MouseX//25*25,MouseY//25*25])
	pygame.display.update()


# for i in range(100, 600, 25):
# 	pygame.draw.rect(Window, (i,0,0), [0,i,25,25])
# 	pygame.draw.rect(Window, (0,i,0), [25,i,25,25])
# 	pygame.draw.rect(Window, (0,0,i), [50,i,25,25])
# 	pygame.draw.rect(Window, (i,0,0), [75,i,25,25])
# 	pygame.draw.rect(Window, (0,i,0), [100,i,25,25])
# 	pygame.draw.rect(Window, (0,0,i), [125,i,25,25])
# 	pygame.draw.rect(Window, (i,0,0), [150,i,25,25])
# 	pygame.draw.rect(Window, (0,i,0), [175,i,25,25])
# 	pygame.draw.rect(Window, (0,0,i), [200,i,25,25])
# 	pygame.draw.rect(Window, (i,0,0), [225,i,25,25])
# 	pygame.draw.rect(Window, (0,i,0), [250,i,25,25])
# 	pygame.draw.rect(Window, (0,0,i), [275,i,25,25])
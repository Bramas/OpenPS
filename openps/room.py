import openps as ops
import pygame, sys

#classe modélisant les Cartes Pièces
class Room:

	# possible walls:
	WALL        = 1
	OPEN        = 2
	CLOSED_DOOR = 3
	OPENED_DOOR = 4

	# room types
	EMPTY       = "Vide"
	RUN         = "Course"
	PARASITE    = "Parasite"
	STORAGE     = "Entrepôt"
	TEAM        = "Fouille en Equipe"
	TERMINAL    = "Terminal"
	REACTOR     = "Réacteur"
	SICK_BAY    = "Infirmerie"
	HIVE        = "Nid"


	def __init__(self, type, walls):
		self.type = type
		self.search = False
		self.walls = walls
	
	
	def __str__(self):
		return self.type+" "+str(self.walls)
	def __repr__(self):
		return self.__str__()

	def draw(self, screen, position):
		x = position[0]*100+300
		y = position[1]*150+300
		pygame.draw.rect(screen, (255,255,255), (x,y,100,150), 0)
		if self.walls[0] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x+10,y)], 1)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x+30,y)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x+70,y), (x+100,y)], 4)

		if self.walls[2] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y+150), (x+100,y+150)], 1)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y+150), (x+30,y+150)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x+70,y+150), (x+100,y+150)], 4)

		if self.walls[1] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x+100,y), (x+100,y+150)], 1)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x+100,y), (x+100,y+60)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x+100,y+90), (x+100,y+150)], 4)

		if self.walls[3] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x,y+150)], 1)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x,y+60)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x,y+90), (x,y+150)], 4)





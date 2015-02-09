# -*- coding:utf8 -*-
import pygame, sys
import collections


#classe modélisant les Cartes Pieces
class Room:

	# wall directions
	NORTH       = 0
	EAST        = 1
	SOUTH       = 2
	WEST        = 3

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
		self.position = None
		self.characters = set()
	
	
	def __str__(self):
		return self.type+" "+str(self.walls)
	def __repr__(self):
		return self.__str__()

	def place_character(self, character):
		self.characters.add(character)
	def remove_character(self, character):
		self.characters.remove(character)

	def update(self, screen, position, preview=False):
		x = position[0]*100+300
		y = position[1]*150+300
		
		background = (255,255,255)
		if preview:
			background = (55,55,55)

		pygame.draw.rect(screen, background, (x,y,100,150), 0)
		if self.walls[Room.NORTH] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x+100,y)], 4)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x+30,y)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x+70,y), (x+100,y)], 4)

		if self.walls[Room.EAST] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x+100,y), (x+100,y+150)], 4)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x+100,y), (x+100,y+60)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x+100,y+90), (x+100,y+150)], 4)

		if self.walls[Room.SOUTH] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y+150), (x+100,y+150)], 4)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y+150), (x+30,y+150)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x+70,y+150), (x+100,y+150)], 4)

		if self.walls[Room.WEST] == Room.WALL:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x,y+150)], 4)
		else:
			pygame.draw.lines(screen, (150,150,150), False, [(x,y), (x,y+60)], 4)
			pygame.draw.lines(screen, (150,150,150), False, [(x,y+90), (x,y+150)], 4)

		x,y = x+5, y+5
		for character in self.characters:
			character.update(screen, (x,y))
			y += 35

	def walkable(self, direction):
		return self.walls[direction] == Room.OPEN or self.walls[direction] == Room.OPENED_DOOR




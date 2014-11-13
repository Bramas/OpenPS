import openps as ops
import pygame, sys

class Board:

	def __init__(self):
		self.rooms = {}

	def place_room(self, room, position):
		if not position[0] in self.rooms:
			self.rooms[position[0]] = {}

		if not position[1] in self.rooms[position[0] ]:
			self.rooms[position[0]][position[1]] = None

		if self.rooms[position[0]][position[1]] != None:
			ops.error("Cannot place a room where there is already a room")
			return

		self.rooms[position[0]][position[1]] = room

	def draw(self, screen):
		for x in self.rooms:
			for y in self.rooms[x]:
				self.rooms[x][y].draw(screen, (x,y))

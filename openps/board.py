# -*- coding:utf8 -*-
import pygame, sys
from . import glb as ops
from .room import Room



class Board:

	def __init__(self):
		self.rooms = {}
		self.room_preview = None
		self.room_preview_positions = []
		self.font = pygame.font.SysFont('verdana', 12) 

	def place_room(self, room, position):
		if position in self.rooms:
			glb.error("Cannot place a room where there is already a room")
			return
		self.rooms[position] = room
		room.position = position


	def move_character(self, character, room):
		if character.room != None:
			character.room.remove(character)
		room.place_character(character)
		character.room = room

	def update(self, screen):
		for position in self.rooms:
			self.rooms[position].update(screen, position)

		for position in self.room_preview_positions:
			self.room_preview.update(screen, position, preview=True)

		if self.room_preview:
			textSurfaceObj = self.font.render("Retourner", True,  (0, 0, 0))
			textRect = pygame.Rect(100, 100, 130, 50)
			screen.blit(textSurfaceObj, textRect)


	def __can_place_room(self, r, x, y):

		# if there is a room at (x,y) we cannot place the room
		if (x, y) in self.rooms:
			return False

		# otherwise we have to check for every adjacent room if it is coherent
		# (and there must be at least one adjacent room)
		is_there_at_least_one_room = False
		if (x-1, y) in self.rooms:
			is_there_at_least_one_room = True
			if not r.explorable(Room.WEST) \
				or not self.rooms[(x-1, y)].explorable(Room.EAST) \
				or (r.walls[Room.WEST] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] \
					and self.rooms[(x-1, y)].walls[Room.EAST] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] ):
				#deux portes blindées ne peuvent être adjacentes
				return False
		if (x+1, y) in self.rooms:
			is_there_at_least_one_room = True
			if not r.explorable(Room.EAST) \
				or not self.rooms[(x+1, y)].explorable(Room.WEST) \
				or (r.walls[Room.EAST] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] \
					and self.rooms[(x+1, y)].walls[Room.WEST] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] ):
				return False
		if (x, y-1) in self.rooms:
			is_there_at_least_one_room = True
			if not r.explorable(Room.NORTH) \
				or not self.rooms[(x, y-1)].explorable(Room.SOUTH) \
				or (r.walls[Room.NORTH] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] \
					and self.rooms[(x, y-1)].walls[Room.SOUTH] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] ):
				return False
		if (x, y+1) in self.rooms:
			is_there_at_least_one_room = True
			if not r.explorable(Room.SOUTH) \
				or not self.rooms[(x, y+1)].explorable(Room.NORTH) \
				or (r.walls[Room.SOUTH] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] \
					and self.rooms[(x, y+1)].walls[Room.NORTH] in [Room.CLOSED_DOOR,Room.OPENED_DOOR] ):
				return False
		return is_there_at_least_one_room

	def set_room_preview(self, preview_room):
		self.room_preview = preview_room
		self.room_preview_positions = []
		if self.room_preview:
			ops.debug(str(self.room_preview.type))
			ops.debug(str(self.room_preview.walls))

		# compute possible positions for the preview_room
		for x in range(-20,21):
			for y in range(-20,21):
				if self.__can_place_room(self.room_preview, x, y):
					self.room_preview_positions.append((x, y))
		
		ops.debug(str(len(self.room_preview_positions))+' room preview')

			

	def turn_preview_card(self):
		if not self.room_preview:
			return False

		self.room_preview = Room(self.room_preview.type, (
			self.room_preview.walls[2],
			self.room_preview.walls[3],
			self.room_preview.walls[0],
			self.room_preview.walls[1]))
		self.set_room_preview(self.room_preview)
		return len(self.room_preview_positions) > 0

	def discover_room(self, position):
		if not self.room_preview:
			return

		self.place_room(self.room_preview, position)

		self.room_preview_positions = []
		self.room_preview = None

	def on_mouse_press(self, position):
		if pygame.Rect(100, 100, 130, 50).collidepoint(position):
			self.turn_preview_card()

		for room_position in self.room_preview_positions:
			x = room_position[0]*100+300
			y = room_position[1]*150+300
			if pygame.Rect(x,y,100,150).collidepoint(position):
				self.discover_room(room_position)
				break
		return

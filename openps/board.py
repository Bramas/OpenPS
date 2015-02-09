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
			if self.room_preview and len(self.room_preview_positions) == 0:
				self.room_preview.update(screen, (-2,-1))



	def set_room_preview(self, preview_room):
		self.room_preview = preview_room
		self.room_preview_positions = []
		if self.room_preview:
			ops.debug(str(self.room_preview.type))
			ops.debug(str(self.room_preview.walls))

		# compute possible positions for the preview_room
		for (x,y) in self.rooms:
			if not (x-1, y) in self.rooms:
				if preview_room.walkable(Room.EAST) \
					and self.rooms[(x, y)].walkable(Room.WEST):
					self.room_preview_positions.append((x-1, y))
			if not (x+1, y) in self.rooms:
				if preview_room.walkable(Room.WEST) \
					and self.rooms[(x, y)].walkable(Room.EAST):
					self.room_preview_positions.append((x+1, y))
			if not (x, y-1) in self.rooms:
				if preview_room.walkable(Room.SOUTH) \
					and self.rooms[(x, y)].walkable(Room.NORTH):
					self.room_preview_positions.append((x, y-1))
			if not (x, y+1) in self.rooms:
				if preview_room.walkable(Room.NORTH) \
					and self.rooms[(x, y)].walkable(Room.SOUTH):
					self.room_preview_positions.append((x, y+1))

		if len(self.room_preview_positions) == 0:
			ops.debug("no preview for this room")
			

	def turn_preview_card(self):
		if not self.room_preview:
			return

		self.room_preview = Room(self.room_preview.type, (
			self.room_preview.walls[2],
			self.room_preview.walls[3],
			self.room_preview.walls[0],
			self.room_preview.walls[1]))
		self.set_room_preview(self.room_preview)

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

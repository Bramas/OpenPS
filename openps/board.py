import openps as ops
import pygame, sys

class Board:

	def __init__(self):
		self.rooms = {}
		self.room_preview = None
		self.room_preview_positions = []

	def place_room(self, room, position):
		if position in self.rooms:
			ops.error("Cannot place a room where there is already a room")
			return
		self.rooms[position] = room

	def draw(self, screen):
		for position in self.rooms:
			self.rooms[position].draw(screen, position)

		for position in self.room_preview_positions:
			self.room_preview.draw(screen, position, preview=True)

	def set_room_preview(self, preview_room):
		self.room_preview_positions = []

		# compute possible positions for the preview_room
		for (x,y) in self.rooms:
			if not (x-1, y) in self.rooms:
				if preview_room.walkable(ops.Room.EAST) \
					and self.rooms[(x, y)].walkable(ops.Room.WEST):
					self.room_preview_positions.append((x-1, y))
			if not (x+1, y) in self.rooms:
				if preview_room.walkable(ops.Room.WEST) \
					and self.rooms[(x, y)].walkable(ops.Room.EAST):
					self.room_preview_positions.append((x+1, y))
			if not (x, y-1) in self.rooms:
				if preview_room.walkable(ops.Room.SOUTH) \
					and self.rooms[(x, y)].walkable(ops.Room.NORTH):
					self.room_preview_positions.append((x, y-1))
			if not (x, y+1) in self.rooms:
				if preview_room.walkable(ops.Room.NORTH) \
					and self.rooms[(x, y)].walkable(ops.Room.SOUTH):
					self.room_preview_positions.append((x, y+1))

		if len(self.room_preview_positions) > 0:
			self.room_preview = preview_room

	def on_mouse_press(self, position):
		return
import pygame, sys
from . import character
from . import glb
from . import player
from .room import Room
from .item import Item

class IA(player.Player):
	def play(self):
		glb.log("Player %d (IA) plays", self.id)

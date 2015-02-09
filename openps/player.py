# -*- coding:utf8 -*-
import pygame, sys
from . import character
from . import glb as ops
from .room import Room
from .item import Item
import threading

class Player:

	def __init__(self, game, id):
		
		self.game          = game
		self.id            = id
		self.infection     = False
		self.action_points = 4
		self.ammo          = 0
		self.soldier       = character.Character(self,"Soldier")
		self.android       = character.Character(self,"Androïd")
		self.hand          = [game.draw_item()         for i in range(2)] # draw two cards
		self.is_playing	   = False
		self.play_mutex    = threading.Semaphore()
		
		#tant qu'un parasite est dans la main de départ, on le défausse, on place un parasite et on tire une autre carte
		
		#si l'Hôte est tiré, self.infection = False
		
		self.hand         += [Item(Item.BLOOD, blood_player=id) for i in range(3)] # and take your 3 blood cards

		ops.debug("Player %d:\n - hand: "+str(self.hand), id)
		self.font = ops.DefaultFont

	def update(self, screen):

		x = 100
		for card in self.hand: 
			cardRect = pygame.Rect(x, screen.get_height() - 50, 130, 150)
			if cardRect.collidepoint(pygame.mouse.get_pos()):
				cardColor = (255,255,255)
			else:
				cardColor = (205,205,205)

			pygame.draw.rect(screen, cardColor, cardRect, 0)
			pygame.draw.rect(screen, (100,100,100), cardRect, 2)
			textSurfaceObj = self.font.render(card.name, True,  (0, 0, 0))
			cardRect.x+=5
			cardRect.y+=5
			screen.blit(textSurfaceObj, cardRect)
			x += 130

	def on_mouse_press(self, position):
		x = 100
		if position[0] < 10:
			ops.debug("end_turn")
			self.end_turn()
		elif len(self.hand) > 5:
			for card in self.hand: 
				cardRect = pygame.Rect(x, pygame.display.get_surface().get_height() - 50, 130, 150)
				x += 130
				if cardRect.collidepoint(position):
					if card.need_target():
						ops.debug("Play %s that need a target", card.name)
					else:
						ops.debug("Play %s", card.name)
					self.hand.remove(card)
					self.game.discard(card)
		else:
			self.search()

	def attack(self):
		ops.log("Player %d attacks", self.id)

	def search(self):
		ops.log("Player %d searchs", self.id)
		card = self.game.draw_item()
		if card.name == Item.PARASITE:
			ops.log("Player %d found a parasite", self.id)
		else:
			ops.log("Player %d found %s", self.id, card.name)
			self.hand.append(card)

	def play(self):
		self.is_playing	   = True
		ops.log("player %d plays", self.id)

	def activate_terminal(self):
		ops.log("Player %d activates the terminal", self.id)

	def heal(self):
		ops.log("Player %d heals", self.id)

	def burn_hive(self):
		ops.log("Player %d burns the hive", self.id)

	def explore(self):
		ops.log("Player %d explores", self.id)
		room = self.game.draw_room()
		ops.debug(str(room))


	def end_turn(self):
		self.game.end_turn(self)

	#def move(self):
	
	#def play_card(self):

	#def skip_turn(self):
		

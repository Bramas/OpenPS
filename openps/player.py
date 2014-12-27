# -*- coding:utf8 -*-
import pygame, sys
from . import character
from . import glb
from .room import Room
from .item import Item

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
		
		#tant qu'un parasite est dans la main de départ, on le défausse, on place un parasite et on tire une autre carte
		
		#si l'Hôte est tiré, self.infection = False
		
		self.hand         += [Item(Item.BLOOD, blood_player=id) for i in range(3)] # and take your 3 blood cards

		glb.debug("Player %d:\n - hand: "+str(self.hand), id)
		self.font = glb.defaultFont

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
		if len(self.hand) > 5:
			for card in self.hand: 
				cardRect = pygame.Rect(x, pygame.display.get_surface().get_height() - 50, 130, 150)
				x += 130
				if cardRect.collidepoint(position):
					if card.need_target():
						glb.debug("Play %s that need a target", card.name)
					else:
						glb.debug("Play %s", card.name)
					self.hand.remove(card)
					self.game.discard(card)
		else:
			self.search()

	def attack(self):
		glb.log("Player %d attacks", self.id)

	def search(self):
		glb.log("Player %d searchs", self.id)
		card = self.game.draw_item()
		if card.name == Item.PARASITE:
			glb.log("Player %d found a parasite", self.id)
		else:
			glb.log("Player %d found %s", self.id, card.name)
			self.hand.append(card)

	def play(self):
		glb.log("player %d plays", self.id)

	def activate_terminal(self):
		glb.log("Player %d activates the terminal", self.id)

	def heal(self):
		glb.log("Player %d heals", self.id)

	def burn_hive(self):
		glb.log("Player %d burns the hive", self.id)

	def explore(self):
		glb.log("Player %d explores", self.id)
		room = self.game.draw_room()
		glb.debug(str(room))

	#def move(self):
	
	#def play_card(self):

	#def skip_turn(self):
		

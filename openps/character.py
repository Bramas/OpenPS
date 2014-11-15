import openps as ops
import pygame, sys

class Character:

	# Classe modélisant les Personnages

	def __init__(self,player,type):
		self.player           = player
		self.type             = type
		self.room             = None
		self.position_in_room = None
		self.health           = 4
		self.weapon           = []
		if self.type=="Androïd":
			self.weapon.append("Gun")
		else:
			self.weapon.append("Flamethrower")

	def update(self, screen, position):
		if self.room == None:
			return

		soldierRect = pygame.Rect(position, (60, 30))
		soldierText = ops.font.render(self.type, True,  (0, 0, 0))
		pygame.draw.rect(screen, (205,205,205), soldierRect, 0)
		pygame.draw.rect(screen, (100,100,100), soldierRect, 2)
		screen.blit(soldierText, soldierRect)

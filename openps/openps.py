import pygame, sys
from pygame.locals import *
import openps as ops

def run():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('OpenPS')

	card = pygame.image.load("openps/resources/cards/character_jason.jpg")
	DISPLAYSURF.blit(card, (100, 100))
	pygame.display.update()

	game2 = ops.Game(2)

	while True: # main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				pygame.display.update()


import logging
def log(msg, *args):
	print(msg % args)
	#logging.info(msg, args)
def debug(msg, *args):
	print(msg % args)
	#logging.info(msg, args)

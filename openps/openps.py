import pygame, sys
from pygame.locals import *
import openps as ops

def run():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('OpenPS')

	game = ops.Game(4)

	while True: # main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				pygame.display.update()
		game.draw(DISPLAYSURF)
		pygame.display.flip()


import logging
def log(msg, *args):
	print(msg % args)
	#logging.info(msg, args)
def debug(msg, *args):
	print(msg % args)
	#logging.info(msg, args)

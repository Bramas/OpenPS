import pygame, sys
from pygame.locals import *
import openps as ops

def run():
	pygame.init()
	ops.font = pygame.font.SysFont('verdana', 12) 
	DISPLAYSURF = pygame.display.set_mode((1024, 780))
	pygame.display.set_caption('OpenPS')

	game = ops.Game(4)

	while True: # main game loop
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				game.on_mouse_press(pygame.mouse.get_pos())
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()
				pygame.display.update()
		DISPLAYSURF.fill((255,255,255))
		game.update(DISPLAYSURF)
		pygame.display.flip()


import logging
def log(msg, *args):
	print(msg % args)
	#logging.info(msg, args)
def debug(msg, *args):
	print(msg % args)
	#logging.info(msg, args)


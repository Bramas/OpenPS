import pygame, sys
from pygame.locals import *
from . import glb as ops
from . import game


#from openps import openps as ops

def run():
	game.Game(4)
	DISPLAYSURF = pygame.display.set_mode((1280, 780))
	pygame.display.set_caption('OpenPS')


	while True: # main game loop
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				game.Game().on_mouse_press(pygame.mouse.get_pos())
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()
				pygame.display.update()
		DISPLAYSURF.fill((255,255,255))
		game.Game().update(DISPLAYSURF)
		pygame.display.flip()



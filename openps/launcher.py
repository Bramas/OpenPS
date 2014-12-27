import pygame, sys
from pygame.locals import *
from . import game
from . import glb
#from openps import openps as ops

def run():
	pygame.init()
	glb.defaultFont = pygame.font.Font("openps/resources/fonts/Regan Slab Medium.ttf", 12) 
	DISPLAYSURF = pygame.display.set_mode((1024, 780))
	pygame.display.set_caption('OpenPS')

	glb.game = game.Game(4)

	while True: # main game loop
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				glb.game.on_mouse_press(pygame.mouse.get_pos())
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()
				pygame.display.update()
		DISPLAYSURF.fill((255,255,255))
		glb.game.update(DISPLAYSURF)
		pygame.display.flip()



import pygame, sys
from pygame.locals import *
from . import glb as ops
from . import game
from .gamelauncher import GameLauncher

#from openps import openps as ops

currentScene = None

def run():
	currentScene = GameLauncher()
	DISPLAYSURF = pygame.display.set_mode((1280, 780))
	pygame.display.set_caption('OpenPS')

	while True: # main game loop
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				currentScene.on_mouse_press(pygame.mouse.get_pos())
			elif event.type == QUIT:
				pygame.quit()
				sys.exit()
				pygame.display.update()
		DISPLAYSURF.fill((255,255,255))
		currentScene.update(DISPLAYSURF)
		pygame.display.flip()
		if currentScene.nextScene:
			currentScene = currentScene.nextScene



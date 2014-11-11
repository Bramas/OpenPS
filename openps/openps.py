
import pygame, sys
from pygame.locals import *

def run():
	pygame.init()
	DISPLAYSURF = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('OpenPS')

	card = pygame.image.load("openps/resources/cards/character_jason.jpg")
	DISPLAYSURF.blit(card, (100, 100))
	pygame.display.update()

	while True: # main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
				pygame.display.update()

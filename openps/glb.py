import pygame, sys
from pygame.locals import *



import logging
def log(msg, *args):
	print(msg % args)
	#logging.info(msg, args)
def debug(msg, *args):
	print(msg % args)
	#logging.info(msg, args)

DefaultFont = pygame.font.Font("openps/resources/fonts/Regan Slab Medium.ttf", 12) 

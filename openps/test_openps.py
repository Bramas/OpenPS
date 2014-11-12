import pygame

class Game(object):
	def main(self,screen):
		image = pygame.image.load('C:\Jeux et Logiciels\Geany\Mesprogrammes\character_jason.jpg')
		while 1:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return
				if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
					return
			screen.fill((200,200,200))
			screen.blit(image,(320,240))
			pygame.display.flip()

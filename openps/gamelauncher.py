# -*- coding:utf8 -*-
# -*- coding:utf8 -*-
import random
import pygame, sys

from .game import Game
from . import glb as ops

import legume
from time import sleep
import time
from .shared.message import ServerMessage

PORT = 29050

class GameLauncher:

	def message_handler(self, sender, args):
		if legume.messages.message_factory.is_a(args, 'ServerMessage'):
			m = ServerMessage()
			m.state.value=ServerMessage.STATE_READY
			self.client.send_reliable_message(m)

			#print("player id: "+str(args.player_id.value)+" state: "+str(args.state.value))
			self.current_player_id = args.player_id.value
		else:
			print('Message: %s' % args)

	def __init__(self):
		#deterministic randomness:
		#random.seed()
		self.nextScene = None

		print('Connecting to server...')
		t = time.time()
		self.client = legume.Client()
		self.client.OnMessage += self.message_handler
		self.client.connect(('localhost', PORT))
		while self.client.state != self.client.ERRORED:
			self.client.update()
			if (self.client.state == self.client.CONNECTED):
				print('Connected to server')
				break
			time.sleep(0.0001)
		if (self.client.state == self.client.ERRORED):
			print('Connection Error')
			sys.exit()

		print('Waiting Player Id')
		self.current_player_id = None
		while self.current_player_id == None:
			self.client.update()
			time.sleep(0.0001)

		print('Player Id = '+str(self.current_player_id))



	def update(self, screen):
		self.client.update()

		textSurfaceObj = ops.DefaultFont.render("Start", True,  (0, 0, 0))
		textRect = pygame.Rect(100, 50, 130, 50)
		screen.blit(textSurfaceObj, textRect)

	def on_mouse_press(self, position):

		if pygame.Rect(100, 50, 130, 50).collidepoint(position):
			self.nextScene = Game(4, self.current_player_id)

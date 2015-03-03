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
from .shared.message import ServerCommand
from . import player

PORT = 29050

class GameLauncher:

	def message_handler(self, sender, args):
		if legume.messages.message_factory.is_a(args, 'ServerMessage'):
			self.server_message = args
		else:
			print('Message: %s' % args)

	def __init__(self):
		#deterministic randomness:
		#random.seed()
		self.nextScene = None
		self.server_message = None

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

		print('Waiting HELLO Response')
		self.current_player_id = None
		while self.server_message == None:
			self.client.update()
			time.sleep(0.0001)

		print('State = '+str(self.server_message.state.value))

	def start_game(self):
		#deterministic randomness:
		random.seed(self.server_message.seed.value)
		ops.debug("Creating game with seed="+str(self.server_message.seed.value))

		players = []
		for i in range(2):
			if i == self.server_message.player_id.value:
				players.append(player.LocalPlayer(i, self.client))
			else:
				players.append(player.DistantPlayer(i, self.client))
				#players.append(ia.IA(self, i))
		self.nextScene = Game(players)

	def update(self, screen):
		self.client.update()

		if self.server_message.state.value == ServerMessage.IN_GAME:
			self.start_game()

		if self.server_message.state.value == ServerMessage.IN_ROOM:
			textSurfaceObj = ops.DefaultFont.render("Start Game", True,  (0, 0, 0))
			textRect = pygame.Rect(100, 150, 130, 50)
			screen.blit(textSurfaceObj, textRect)
		else:
			textSurfaceObj = ops.DefaultFont.render("Create Game", True,  (0, 0, 0))
			textRect = pygame.Rect(100, 50, 130, 50)
			screen.blit(textSurfaceObj, textRect)

			textSurfaceObj = ops.DefaultFont.render("Join Game", True,  (0, 0, 0))
			textRect = pygame.Rect(100, 100, 130, 50)
			screen.blit(textSurfaceObj, textRect)

	def on_mouse_press(self, position):

		if self.server_message.state.value != ServerMessage.IN_ROOM and pygame.Rect(100, 50, 130, 50).collidepoint(position):
			c = ServerCommand()
			c.command.value = ServerCommand.CREATE_ROOM
			self.client.send_reliable_message(c)

		if self.server_message.state.value != ServerMessage.IN_ROOM and pygame.Rect(100, 100, 130, 50).collidepoint(position):
			c = ServerCommand()
			c.command.value = ServerCommand.FIND_ROOM
			self.client.send_reliable_message(c)

		if self.server_message.state.value == ServerMessage.IN_ROOM and pygame.Rect(100, 150, 130, 50).collidepoint(position):
			c = ServerCommand()
			c.command.value = ServerCommand.START_GAME
			self.client.send_reliable_message(c)


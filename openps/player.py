# -*- coding:utf8 -*-
import pygame, sys
from . import character
from . import glb as ops
from .room import Room
from .item import Item
import threading
import legume
from openps.shared.message import PlayerMessage

class Player:
	END_TURN = 1
	SEARCH = 2
	EXPLORE = 3
	DISCOVER = 4

	def __init__(self, id, client):
		
		self.client        = client
		self.id            = id
		self.infection     = False
		self.action_points = 4
		self.ammo          = 0
		self.soldier       = character.Character(self,"Soldier")
		self.android       = character.Character(self,"Androïd")
		self.is_playing	   = False
		self.play_mutex    = threading.Semaphore()
		self.failed_explore= False

		self.client.OnMessage += self._message_handler
		
		#tant qu'un parasite est dans la main de départ, on le défausse, on place un parasite et on tire une autre carte
		
		#si l'Hôte est tiré, self.infection = False
		

		self.font = ops.DefaultFont

	def on_game_init(self, game):
		self.game = game
		self.hand  = [self.game.draw_item() for i in range(2)] # draw two cards
		self.hand += [Item(Item.BLOOD, blood_player=self.id) for i in range(3)] # and take your 3 blood cards
		ops.debug("Player %d:\n - hand: "+str(self.hand), self.id)

	def _message_handler(self, sender, args):
		if legume.messages.message_factory.is_a(args, 'PlayerMessage'):
			if args.player_id.value == self.id:
				self.on_message(args)


	def update(self, screen):
		self.client.update()
	

	def on_mouse_press(self, position):
		pass

	def attack(self):
		ops.log("Player %d attacks", self.id)

	def search(self):
		ops.log("Player %d searchs", self.id)
		card = self.game.draw_item()
		if card.name == Item.PARASITE:
			ops.log("Player %d found a parasite", self.id)
		else:
			ops.log("Player %d found %s", self.id, card.name)
			self.hand.append(card)
		self.on_action(Player.SEARCH)

	def play(self):
		self.is_playing	   = True
		ops.log("player %d plays (%s)", self.id, self.type)

	def activate_terminal(self):
		ops.log("Player %d activates the terminal", self.id)

	def heal(self):
		ops.log("Player %d heals", self.id)

	def burn_hive(self):
		ops.log("Player %d burns the hive", self.id)

	def explore(self):
		ops.log("Player %d explores", self.id)
		room = self.game.draw_room()
		self.on_action(Player.EXPLORE)
	def discover(self, index):
		self.game.board.discover_room(index)
		self.on_action(Player.DISCOVER, index)

	def select_room_preview(self, index):
		pass

	def end_turn(self):
		self.game.end_turn(self)
		self.on_action(Player.END_TURN)


	def on_action(self, action, target=0):
		pass

	def on_message(self, message):
		pass
	def my_turn(self):
		return self.game.current_player.id == self.id

	#def move(self):
	
	#def play_card(self):

	#def skip_turn(self):
		

class LocalPlayer(Player):
	def __init__(self, id, client):
		Player.__init__(self, id, client)
		self.type	= "local player: You"

	def update(self, screen):

		self.client.update()
		x = 100
		for card in self.hand: 
			cardRect = pygame.Rect(x, screen.get_height() - 50, 130, 150)
			if cardRect.collidepoint(pygame.mouse.get_pos()):
				cardColor = (255,255,255)
			else:
				cardColor = (205,205,205)

			pygame.draw.rect(screen, cardColor, cardRect, 0)
			pygame.draw.rect(screen, (100,100,100), cardRect, 2)
			textSurfaceObj = self.font.render(card.name, True,  (0, 0, 0))
			cardRect.x+=5
			cardRect.y+=5
			screen.blit(textSurfaceObj, cardRect)
			x += 130

		if self.my_turn():
			textSurfaceObj = ops.DefaultFont.render("à mon tour", True,  (0, 0, 0))
			textRect = pygame.Rect(300, 00, 130, 50)
			screen.blit(textSurfaceObj, textRect)
		else:
			textSurfaceObj = ops.DefaultFont.render("au tour du joueur "+str(self.game.current_player.id), True,  (0, 0, 0))
			textRect = pygame.Rect(300, 00, 130, 50)
			screen.blit(textSurfaceObj, textRect)


		if not self.game.board.room_preview:
			textSurfaceObj = ops.DefaultFont.render("Explorer", True,  (0, 0, 0))
			textRect = pygame.Rect(100, 50, 130, 50)
			screen.blit(textSurfaceObj, textRect)

	def select_room_preview(self, index):
		if not self.my_turn():
			return
		self.discover(index)

	def on_mouse_press(self, position):
		if not self.my_turn():
			return
		x = 100

		if not self.game.board.room_preview and pygame.Rect(100, 50, 130, 50).collidepoint(position):
			self.explore()
		elif position[0] < 10:
			ops.debug("end_turn")
			self.end_turn()
		elif len(self.hand) > 5:
			for card in self.hand: 
				cardRect = pygame.Rect(x, pygame.display.get_surface().get_height() - 50, 130, 150)
				x += 130
				if cardRect.collidepoint(position):
					if card.need_target():
						ops.debug("Play %s that need a target", card.name)
					else:
						ops.debug("Play %s", card.name)
					self.hand.remove(card)
					self.game.discard(card)
		else:
			self.search()


	def on_action(self, action, target=0):
		c = PlayerMessage()
		c.player_id.value = self.id
		c.action.value = action
		c.target.value = target
		self.client.send_reliable_message(c)
		ops.debug("send Player action %d", action)



class DistantPlayer(Player):
	def __init__(self, id, client):
		Player.__init__(self, id, client)
		self.type	= "distant player"

	def on_message(self, message):
		ops.debug("message: %d", message.action.value)
		if message.action.value == Player.EXPLORE:
			self.explore()
		elif message.action.value == Player.DISCOVER:
			self.discover(message.target.value)
		elif message.action.value == Player.END_TURN:
			self.end_turn()

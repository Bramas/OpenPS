# -*- coding:utf8 -*-
import random
import pygame, sys

from .room import Room
from .item import Item
from . import player
from . import ia
from . import board
from . import glb as ops


class _Game:

	def __init__(self, nb_players, current_player_id):
		#deterministic randomness:
		#random.seed()
		self.nextScene = None
		self.current_player_id = current_player_id
		self.nb_players = nb_players

		#create decks
		self.create_rooms_deck()
		self.create_items_deck()

		#create the players
		self.players = []
		for i in range(nb_players - 1):
			if i == self.current_player_id:
				self.players.append(player.Player(self, i))
			else:
				self.players.append(ia.IA(self, i))

		self.current_player = self.players[current_player_id]

		self.board = board.Board();

		reactor = self.rooms_deck.pop()
		self.board.place_room(reactor, (0,0))

		ops.debug("Game created with %d players", nb_players)





		#test actions
		self.board.move_character(self.current_player.soldier, reactor)
		self.board.move_character(self.current_player.android, reactor)

		self.current_player.play()
		
	def update(self, screen):
		self.board.update(screen)
		self.players[0].update(screen)

		if not self.board.room_preview:
			textSurfaceObj = ops.DefaultFont.render("Explorer", True,  (0, 0, 0))
			textRect = pygame.Rect(100, 50, 130, 50)
			screen.blit(textSurfaceObj, textRect)


	def draw_item(self):
		if len(self.items_deck) == 0:
			# if there is no more card in the deck we move the discard_deck to the deck and then shuffle
			while len(self.discard_deck) > 0:
				self.items_deck.append(self.discard_deck.pop())
			random.shuffle(self.items_deck)

		return self.items_deck.pop()
		
	def draw_room(self):
		if len(self.rooms_deck) == 0:
			ops.debug("no room to draw")
		r=self.rooms_deck.pop()
		
		# compute possible positions for the preview_room

		self.board.set_room_preview(r)
		#si la room peut se placer autour d'une pièce contenant un personnage du joueur actif, on affiche les possibilités
		
		#sinon, s'il existe un autre endroit sur le plan où on peut placer la room, alors :
			#il ne se passe rien, l'action d'exploration échoue.
			
		if len(self.board.room_preview_positions) == 0 \
			and not self.board.turn_preview_card():
				
			#if the room doesn't fit anywhere
			
			ops.debug("no preview for this room")


			if  r.type == Room.HIVE :
				#if it is the Hive, the room is turned 90°
				r.walls = (Room.WALL,Room.OPEN,Room.WALL,Room.WALL)
				self.board.set_room_preview(r)
				
				if len(self.board.room_preview_positions) == 0 \
					and not self.board.turn_preview_card():
					#if the Hive doesn't fit anywhere
					
					if len(self.rooms_deck) == 0 :
						#if it is the last room in the deck
						ops.debug("game over")
					else :
						#if there is at least one other room in the deck,
						#try to set the room after the Hive
						self.rooms_deck.insert(len(self.rooms_deck) - 1,r)
						return self.draw_room()
			elif self.current_player.failed_explore == True :
				#if the player has already failed or used this possibility
				ops.debug("already failed exploration")
				self.board.room_preview = None

			else:
				#put the impossible room at the end of the deck
				#and try to set the next room around his characters
				self.current_player.failed_explore = True
				self.rooms_deck.insert(0,r)
				return self.draw_room()

						
						




	def discard(self, card):
		return self.discard_deck.append(card)

	def on_mouse_press(self, position):
		self.board.on_mouse_press(position)
		self.players[0].on_mouse_press(position)

		if not self.board.room_preview and pygame.Rect(100, 50, 130, 50).collidepoint(position):
			self.draw_room()


	def end_turn(self, player):
		if player == self.current_player:
			ops.debug('player %d ended the turn', self.current_player.id)
			self.current_player = self.players[(self.current_player.id + 1)%self.nb_players]
			self.current_player.play()
		else:
			ops.debug('wrong player ended the turn')

	#construction of the deck of rooms
	def create_rooms_deck(self):
		
		#doors : [North,West,South,East,Up,Down]
		
		rooms_distribution = {
			Room.RUN          : [
				(Room.CLOSED_DOOR, Room.OPEN, Room.WALL, Room.WALL),
				(Room.OPEN, Room.OPEN, Room.OPEN, Room.OPEN),
				(Room.OPEN, Room.OPEN, Room.OPEN, Room.OPEN)],
			Room.TEAM         : [
				(Room.WALL, Room.WALL, Room.OPEN, Room.OPEN),
				(Room.OPEN, Room.CLOSED_DOOR, Room.WALL, Room.OPEN),
				(Room.OPEN, Room.OPEN, Room.WALL, Room.WALL),
				(Room.CLOSED_DOOR, Room.WALL, Room.OPEN, Room.WALL)],
			Room.PARASITE     : [
				(Room.OPEN, Room.OPEN, Room.WALL, Room.OPEN),
				(Room.OPEN, Room.WALL, Room.OPEN, Room.OPEN),
				(Room.WALL, Room.WALL, Room.OPEN, Room.OPEN),
				(Room.WALL, Room.OPEN, Room.OPEN, Room.OPEN)],
			Room.EMPTY        : [
				(Room.OPEN, Room.OPEN, Room.WALL, Room.OPEN),
				(Room.OPEN, Room.CLOSED_DOOR, Room.CLOSED_DOOR, Room.OPEN)],
			Room.STORAGE      : [
				(Room.WALL, Room.WALL, Room.OPEN, Room.OPEN),
				(Room.OPEN, Room.OPEN, Room.WALL, Room.OPEN)],
			Room.SICK_BAY     : [
				(Room.WALL, Room.WALL, Room.OPEN, Room.WALL)],
			Room.TERMINAL     : [
				(Room.WALL, Room.WALL, Room.OPEN, Room.WALL)]
		}
		hive     = Room(Room.HIVE   ,  (Room.WALL, Room.WALL, Room.OPEN, Room.WALL))
		reactor  = Room(Room.REACTOR,  (Room.OPEN, Room.OPEN, Room.OPEN, Room.OPEN))
		terminal = Room(Room.TERMINAL, (Room.WALL, Room.OPEN, Room.OPEN, Room.OPEN))
		
		self.rooms_deck = []
		for type, l in rooms_distribution.items():
			for wall in l:
				self.rooms_deck.append(Room(type, wall))
		random.shuffle(self.rooms_deck)

		#add Terminal (one room) amongst the second half
		self.rooms_deck.insert(random.randint(0,9), terminal)

		#add hive amongst the three last cards
		self.rooms_deck.insert(random.randint(0,2), hive)
		#add Reacteur on top
		self.rooms_deck.append(reactor)

	#construction of the deck of items
	def create_items_deck(self):
		base_item_distribution = {
			Item.JERRY      :12,
			Item.VEST       :7,
			Item.MUNITION   :6,
			Item.PARASITE   :3,
			Item.HEALTH_KIT :3,
			Item.MAGNET     :3,
			Item.MACHINE_GUN:2,
			Item.GRENADE    :2,
			Item.ADRENALINE :2,
			Item.GLASSES    :2,
			Item.KNIFE      :2,
			Item.SCANNER    :1
		}
		base_deck = []
		for item, count in base_item_distribution.items():
			base_deck += [Item(item) for i in range(count)]
		top_deck = [Item(Item.HOST)]

		for i in range(self.nb_players):
			top_deck.append(base_deck.pop(0)) # transfert a jerry

		random.shuffle(base_deck)
		for i in range(2 * self.nb_players - 1):
			top_deck.append(base_deck.pop())

		random.shuffle(top_deck)
		self.items_deck = top_deck
		self.discard_deck = base_deck




class _GameInstance:
	instance = None
	def __init__(self, nb_players, current_player_id):
		if not _GameInstance.instance:
			_GameInstance.instance = _Game(nb_players, current_player_id)



def Game(nb_players = None, current_player_id = None):
	_GameInstance(nb_players, current_player_id)
	return _GameInstance.instance

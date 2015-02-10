
import random
import pygame, sys

from .room import Room
from .item import Item
from . import player
from . import ia
from . import board
from . import glb as ops

class _Game:

	def __init__(self, nb_players):
		#deterministic randomness:
		#random.seed()
		
		self.nb_players = nb_players

		#create decks
		self.create_rooms_deck()
		self.create_items_deck()

		#create the players
		playerId = 0
		self.players = []
		self.players.append(player.Player(self, playerId))
		for i in range(nb_players - 1):
			playerId += 1
			self.players.append(ia.IA(self, playerId))

		self.current_player = self.players[0]

		self.board = board.Board();

		reactor = self.rooms_deck.pop()
		self.board.place_room(reactor, (0,0))

		ops.debug("Game created with %d players", nb_players)





		#test actions
		self.board.move_character(self.players[0].soldier, reactor)
		self.board.move_character(self.players[0].android, reactor)

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
		r=self.rooms_deck.pop()
		
		# compute possible positions for the preview_room

		self.board.set_room_preview(r)
			
		if len(self.board.room_preview_positions) == 0:
			#if the room doesn't fit
			ops.debug("no preview for this room")

			#si la room peut se placer autour d'une pièce contenant un personnage du joueur actif, on affiche les possibilités
				#sinon, s'il existe un autre endroit sur le plan où on peut placer la room, alors :
					#il ne se passe rien, l'action d'exploration échoue.
				#s'il n'existe aucun autre endroit où placer la room, alors :
					#soit il s'agit du Hive, alors :
						#on affecte chacune de ses ouvertures à la suivante
						#(North -> West, West -> South, ...)
						#on modifie son aspect (carré à la place de rectangulaire)
					#soit il s'agit d'un autre type, dans ce cas :
						#on met la room sous la pioche
						#on tente de placer la nouvelle room qui est apparue au sommet de la pioche
						#soit on arrive à la placer, soit non, mais on ne fait pas d'autre vérification


	def discard(self, card):
		return self.discard_deck.append(card)

	def on_mouse_press(self, position):
		self.board.on_mouse_press(position)
		self.players[0].on_mouse_press(position)

		if not self.board.room_preview and pygame.Rect(100, 50, 130, 50).collidepoint(position):
			self.draw_room()


	def end_turn(self, player):
		if player == self.current_player:
			glb.debug('player %d ended the turn', self.current_player.id)
			self.current_player = self.players[(self.current_player.id + 1)%self.nb_players]
			self.current_player.play()
		else:
			glb.debug('wrong player ended the turn')

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
	def __init__(self, nb_players):
		if not _GameInstance.instance:
			_GameInstance.instance = _Game(nb_players)



def Game(nb_players = None):
	_GameInstance(nb_players)
	return _GameInstance.instance

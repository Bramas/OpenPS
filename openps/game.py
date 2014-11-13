import openps as ops

import random

class Game:

	def __init__(self, nb_players):
		#deterministic randomness:
		#random.seed()
		
		self.nb_players = nb_players

		#create decks
		self.create_rooms_deck()
		self.create_items_deck()

		#create the players
		self.players = [ ops.Player(self, i) for i in range(nb_players)]

		ops.debug("Game created with %d players", nb_players)
		

	def draw_item(self):
		return self.items_deck.pop()


	#construction of the deck of rooms
	def create_rooms_deck(self):
		self.rooms_deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
		random.shuffle(self.rooms_deck)
		#add Terminal (one room) amongst the second half
		self.rooms_deck.insert(random.randint(0,9),17)
		#add Nid amongst the three last cards
		self.rooms_deck.insert(random.randint(0,2),18)
		#add Réacteur on top
		self.rooms_deck.append(19)

	#construction of the deck of items
	def create_items_deck(self):
		base_item_distribution = {
			ops.Item.JERRY      :12,
			ops.Item.VEST       :7,
			ops.Item.MUNITION   :6,
			ops.Item.PARASITE   :3,
			ops.Item.HEALTH_KIT :3,
			ops.Item.MAGNET     :3,
			ops.Item.MACHINE_GUN:2,
			ops.Item.GRENADE    :2,
			ops.Item.ADRENALINE :2,
			ops.Item.GLASSES    :2,
			ops.Item.KNIFE      :2,
			ops.Item.SCANNER    :1
		}
		base_deck = []
		for item, count in base_item_distribution.items():
			base_deck += [ops.Item(item) for i in range(count)]
		top_deck = [ops.Item(ops.Item.HOST)]

		for i in range(self.nb_players):
			top_deck.append(base_deck.pop(0)) # transfert a jerry

		random.shuffle(base_deck)
		for i in range(2 * self.nb_players - 1):
			top_deck.append(base_deck.pop())

		random.shuffle(top_deck)
		self.items_deck = top_deck
		self.discard = base_deck
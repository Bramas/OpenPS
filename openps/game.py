import openps as ops

import random

class Game:

	def __init__(self, nb_players):
		#deterministic randomness:
		random.seed()
		self.nb_players = nb_players

		#construction of the deck of rooms
		rooms_deck = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
		random.shuffle(rooms_deck)
		#add Terminal (one room) amongst the second half
		rooms_deck.insert(random.randint(0,9),17)
		#add Nid amongst the three last cards
		rooms_deck.insert(random.randint(0,2),18)
		#add Réacteur on top
		rooms_deck.append(19)
		#complete

		#construction of the deck of items
		base_deck = [1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8,9,9,10,10,11,11,12]
		top_deck  = [13]
		for i in range(nb_players):
			base_deck.remove(1)
			top_deck.append(1)

		random.shuffle(base_deck)
		for i in range(2 * nb_players - 1):
			top_deck.append(base_deck.pop())

		random.shuffle(top_deck)
		self.items_deck = base_deck + top_deck
		#complete

		#create the players
		self.players = [ ops.Player(self, i) for i in range(nb_players)]

		ops.debug("Game created with %d players", nb_players)
		

	def draw_item(self):
		return self.items_deck.pop()

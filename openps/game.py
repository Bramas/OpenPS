import openps as ops

import random

class Game:

	def __init__(self, nb_players):
		#deterministic randomness:
		#random.seed(1)
		self.nb_players = nb_players
		self.room = []
		self.itemsdeck=[1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,8,8,9,9,10,10,11,11,12]
		self.startingitemsdeck=[13]
		for i in range(nb_players):
			self.itemsdeck.remove(1)
			self.startingitemsdeck.append(1)
		random.shuffle(self.itemsdeck)
		for i in range(2*nb_players-1):
			self.startingitemsdeck.append(self.itemsdeck.pop())
		random.shuffle(self.startingitemsdeck)
		
		self.players = [ ops.Player(self, i) for i in range(nb_players)]
		
		self.itemsdeck+=self.startingitemsdeck
		del self.startingitemsdeck
		
		ops.log("Game created with %d players", nb_players)

	def draw_item(self):
		return self.startingitemsdeck.pop()

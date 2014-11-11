import openps as ops

import random

class Game:

	def __init__(self, nb_players):
		#deterministic randomness:
		#random.seed(1)
		self.nb_players = nb_players
		self.locations = []
		self.objects = [1,2,3,4,5,6,7]
		random.shuffle(self.objects)

		self.players = [ ops.Player(self, i, ops.Player.ANDROID) for i in range(nb_players)]
		ops.log("Game created with %d players", nb_players)

	def draw_object(self):
		return self.objects.pop()
import openps as ops


class Player:
	# player types:
	ANDROID = 0
	SOLDIER = 1

	def __init__(self, game, id, type):
		self.game = game
		self.id = id
		self.type = type
		self.pv = 4
		self.hand = [game.draw_object() for i in range(2)]
		ops.log("Player %d:\n - hand: "+str(self.hand), id)
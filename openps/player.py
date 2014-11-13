import openps as ops

class Player:

	def __init__(self, game, id):
		
		self.game          = game
		self.id            = id
		self.action_points = 4
		self.soldier       = ops.Character(self,"Soldier")
		self.android       = ops.Character(self,"Androïd")
		self.hand          = [game.draw_item()         for i in range(2)] # draw two cards
		self.hand         += [ops.Item(ops.Item.BLOOD, blood_player=id) for i in range(3)] # and take your 3 blood cards

		ops.debug("Player %d:\n - hand: "+str(self.hand), id)

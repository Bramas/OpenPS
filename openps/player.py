import openps as ops

class Player:

	def __init__(self, game, id):
<<<<<<< HEAD
		self.game = game
		self.id = id
		self.pa = 4
		self.soldier=ops.Character(self,"Soldier")
		self.android=ops.Character(self,"Androïd")
		
		self.hand = [game.draw_item() for i in range(2)]
		
		ops.log("Player %d:\n - hand: "+str(self.hand), id)
=======
		self.game          = game
		self.id            = id
		self.action_points = 4
		self.soldier       = ops.Character(self,"Soldier")
		self.android       = ops.Character(self,"Androïd")
		self.hand          = [game.draw_object() for i in range(2)]

		ops.debug("Player %d:\n - hand: "+str(self.hand), id)
>>>>>>> 6336d7cf06f1ccbf6bd2392493ae0fabdef5a9e6

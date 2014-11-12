import openps as ops

class Character:

	# Classe modélisant les Personnages

	def __init__(self,player,type):
		self.player           = player
		self.type             = type
		self.room             = None
		self.position_in_room = None
		self.health           = 4
		self.weapon           = []
		if self.type=="Androïd":
			self.weapon.append("Gun")
		else:
			self.weapon.append("Flamethrower")

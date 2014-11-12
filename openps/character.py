import openps as ops

class Character:
	
	# Classe modélisant les Personnages
	
	def __init__(self,player,type):
		self.player = player
		self.type = type
		self.location=[]
		self.pv = 4
		self.weapon=[]
		if self.type=="Androïd":
			self.weapon.append("Gun")
		else:
			self.weapon.append("Flamethrower")

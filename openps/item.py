import openps as ops

class Item:

	JERRY 	    = "Jerrican"
	VEST 	 	= "Gilet Pare-Balles"
	MUNITION 	= "Munitions"
	PARASITE 	= "Alerte Parasites !"
	HEALTH_KIT 	= "Kit de Premiers Soins"
	MAGNET   	= "Carte magnétique"
	MACHINE_GUN = "Fusil Mitrailleur"
	GRENADE  	= "Grenade"
	ADRENALINE 	= "Adrénaline" 
	GLASSES  	= "Lunette de Précision"
	KNIFE 		= "Couteau de Combat"
	SCANNER 	= "Scanner Corporel"
	HOST 		= "Hôte"
	BLOOD 		= "Sang"


	def __init__(self, name, blood_player=None):
		self.name = name
		self.weapon = False
		self.blood=False

		if name in [Item.MACHINE_GUN, Item.GRENADE, Item.KNIFE]:
			self.weapon = True

		if name == Item.BLOOD:
			self.blood = True
			self.blood_player = blood_player

	def need_target(self):
		if self.name in [Item.HEALTH_KIT, Item.SCANNER]:
			return True
		return False

	def __str__(self):
		return self.name
	def __repr__(self):
		return self.__str__()

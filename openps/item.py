import openps as ops

class Item:

	def __init__(self, id):
		self.id = id
		self.weapon = False
		self.blood=False
		if id==1:
			self.name = "Jerrican"
		elif id==2:
			self.name = "Gilet Pare-Balles"
		elif id==3:
			self.name = "Munitions"
		elif id==4:
			self.name = "Alerte Parasites !"
		elif id==5:
			self.name = "Kit de Premiers Soins"
		elif id==6:
			self.name = "Carte magnétique"
		elif id==7:
			self.name = "Fusil Mitrailleur"
			self.weapon = True
		elif id==8:
			self.name = "Grenade"
			self.weapon = True
		elif id==9:
			self.name = "Adrénaline"
		elif id==10:
			self.name = "Lunette de Précision"
		elif id==11:
			self.name = "Couteau de Combat"
			self.weapon = True
		elif id==12:
			self.name = "Scanner Corporel"
		elif id==13:
			self.name = "Hôte"
		else:
			#Chaque joueur obtient en début de partie les trois cartes Sang de sa propre couleur
			self.name = "Sang"

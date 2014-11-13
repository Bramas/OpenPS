import openps as ops

class Room:

	#classe modélisant les Cartes Pièces


	WALL        = 1
	OPEN        = 2
	CLOSED_DOOR = 3
	OPENED_DOOR = 4

	def __init__(self, id):
		self.id = id
		if id==0:
			self.name = "Course"
		elif id==1:
			self.name = "Course"
		elif id==2:
			self.name = "Course"
		elif id==3:
			self.name = "Fouille en Equipe"
		elif id==4:
			self.name = "Fouille en Equipe"
		elif id==5:
			self.name = "Fouille en Equipe"
		elif id==6:
			self.name = "Fouille en Equipe"
		elif id==7:
			self.name = "Parasite"
		elif id==8:
			self.name = "Parasite"
		elif id==9:
			self.name = "Parasite"
		elif id==10:
			self.name = "Parasite"
		elif id==11:
			#L'infirmerie comporte deux pièces
			self.name = "Infirmerie"
		elif id==12:
			self.name = "Entrepôt"
		elif id==13:
			self.name = "Entrepôt"
		elif id==14:
			self.name = "Vide"
		elif id==15:
			self.name = "Vide"
		elif id==16:
			#Terminal constitué de deux pièces
			self.name = "Terminal"
		elif id==17:
			#Terminal consistué d'une pièce
			self.name = "Terminal"
		elif id==18:
			self.name = "Nid"
		else:
			self.name = "Réacteur"

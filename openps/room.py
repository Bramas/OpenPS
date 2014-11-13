import openps as ops

#classe modélisant les Cartes Pièces
class Room:

	# possible walls:
	WALL        = 1
	OPEN        = 2
	CLOSED_DOOR = 3
	OPENED_DOOR = 4

	# room types
	EMPTY       = "Vide"
	RUN         = "Course"
	PARASITE    = "Parasite"
	STORAGE     = "Entrepôt"
	TEAM        = "Fouille en Equipe"
	TERMINAL    = "Terminal"
	REACTOR     = "Réacteur"
	SICK_BAY    = "Infirmerie"
	HIVE        = "Nid"


	def __init__(self, type, walls):
		self.type = type
	
	
	def __str__(self):
		return self.type
	def __repr__(self):
		return self.__str__()

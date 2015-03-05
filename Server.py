import legume
import time
import random
from openps.shared.message import ServerMessage
from openps.shared.message import ServerCommand
from openps.shared.message import PlayerMessage








class ServerRoom:
	def __init__(self):
		self.peers = []



class Server:

	PORT = 29050

	def __init__(self):
		self.peersState = {}
		self.rooms = {}
		self.nextRoomId = 1
		self.games = {}

	def update_peer(self, peer):
		peer.send_reliable_message(self.peersState[peer.address])

	def hello(self, peer):
		m = ServerMessage()
		m.state.value = ServerMessage.WHAT_DO_YOU_WANT
		self.peersState[peer.address] = m
		self.update_peer(peer)

	def create_room(self, peer):
		r = ServerRoom()
		r.peers.append(peer)
		self.peersState[peer.address].room_id.value = self.nextRoomId
		self.peersState[peer.address].state.value = ServerMessage.IN_ROOM
		self.peersState[peer.address].player_id.value = 0
		self.rooms[self.nextRoomId] = r
		self.nextRoomId += 1
		self.update_peer(peer)

	def find_room(self, peer):
		if len(self.rooms) == 0:
			self.peersState[peer.address].state.value = ServerMessage.NOPE
		else:
			for r in self.rooms:
				self.peersState[peer.address].state.value = ServerMessage.IN_ROOM
				self.peersState[peer.address].room_id.value = r
				self.peersState[peer.address].player_id.value = len(self.rooms[r].peers)
				self.rooms[r].peers.append(peer)
				break
		self.update_peer(peer)

	def start_game(self, peer):
		print(str(peer.address)+" start game")
		print("room id: "+str(self.peersState[peer.address].room_id.value))

		r = self.peersState[peer.address].room_id.value

		if not r in self.rooms:
			print("Room "+str(r)+" does not exist")
			return

		self.games[r] = self.rooms[r]
		del self.rooms[r]
		seed = random.random()
		for p in self.games[r].peers:
			self.peersState[p.address].state.value = ServerMessage.IN_GAME
			self.peersState[p.address].seed.value = seed
			print(str(p.address)+" in game")
			self.update_peer(p)


	def message_handler(self, sender, message):
		if message.MessageTypeID == ServerMessage.MessageTypeID:
			print("ServerMessage from "+str(sender.address))
		elif message.MessageTypeID == ServerCommand.MessageTypeID:
			print("command "+str(message.command.value)+" from "+str(sender.address))
			if message.command.value == ServerCommand.CREATE_ROOM:
				self.create_room(sender)
			elif message.command.value == ServerCommand.FIND_ROOM:
				self.find_room(sender)
			elif message.command.value == ServerCommand.START_GAME:
				self.start_game(sender)
		elif message.MessageTypeID == PlayerMessage.MessageTypeID:
			print("player command from "+str(sender.address)+" player id="+str(message.player_id.value))
			if self.peersState[sender.address] and self.peersState[sender.address].state.value == ServerMessage.IN_GAME:
				if self.peersState[sender.address].room_id.value in self.games:
					for p in self.games[self.peersState[sender.address].room_id.value].peers:
						p.send_reliable_message(message)
			


	def run(self):
		s = legume.Server()
		s.OnMessage += self.message_handler
		s.listen(('', Server.PORT))

		t = time.time()
		player_counter = 0
		while True:
			s.update()

			if time.time() > t + 1.0:
				t = time.time()
				for peerAdr in list(self.peersState.keys()):
					found = False
					for peer in s.peers:
						if peer.address == peerAdr:
							found = True
							break
					if not found:
						print("Lost Connexion: "+str(peerAdr)+" player_id: "+str(self.peersState[peerAdr].player_id.value))
						del(self.peersState[peerAdr])

				for peer in s.peers:
					#print(str(peer.address)+" "+str(peer.latency))
					if not peer.address in self.peersState:
						print("New Connexion: "+str(peer.address))
						self.hello(peer)
						
			time.sleep(0.001)


if __name__ == '__main__':
	s = Server()
	s.run()

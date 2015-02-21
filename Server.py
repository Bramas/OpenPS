import legume
import time
from openps.shared.message import ServerMessage
from openps.shared.message import ServerCommand

PORT = 29050





peersState = {}
rooms = []


class ServerRoom:
	def __init__(self):
		self.peers = []


def update_peer(peer):
	peer.send_reliable_message(peersState[peer.address])

def hello(peer):
	m = ServerMessage()
	m.state.value = ServerMessage.WHAT_DO_YOU_WANT
	peersState[peer.address] = m
	update_peer(peer)

def create_room(peer):
	r = ServerRoom()
	r.peers.append(peer)
	peersState[peer.address].room_id.value = len(rooms)
	peersState[peer.address].state.value = ServerMessage.IN_ROOM
	peersState[peer.address].player_id.value = 0
	rooms.append(r)
	update_peer(peer)

def find_room(peer):
	if len(rooms) == 0:
		peersState[peer.address].state.value = ServerMessage.NOPE
	else:
		peersState[peer.address].state.value = ServerMessage.IN_ROOM
		peersState[peer.address].room_id.value = 0
		peersState[peer.address].player_id.value = len(rooms[0].peers)
		rooms[0].peers.append(peer)
	update_peer(peer)

def start_game(peer):
	print(str(peer.address)+" start game")
	print("room id: "+str(peersState[peer.address].room_id.value))
	for p in rooms[peersState[peer.address].room_id.value].peers:
		peersState[p.address].state.value = ServerMessage.IN_GAME
		print(str(p.address)+" in game")
		update_peer(p)


def message_handler(sender, message):
	if message.MessageTypeID == ServerMessage.MessageTypeID:
		print("message from "+str(sender.address))
	elif message.MessageTypeID == ServerCommand.MessageTypeID:
		print("command "+str(message.command.value)+" from "+str(sender.address))
		if message.command.value == ServerCommand.CREATE_ROOM:
			create_room(sender)
		elif message.command.value == ServerCommand.FIND_ROOM:
			find_room(sender)
		elif message.command.value == ServerCommand.START_GAME:
			start_game(sender)


def main():
	s = legume.Server()
	s.OnMessage += message_handler
	s.listen(('', PORT))

	t = time.time()
	player_counter = 0
	while True:
		s.update()

		if time.time() > t + 1.0:
			t = time.time()
			for peerAdr in list(peersState.keys()):
				found = False
				for peer in s.peers:
					if peer.address == peerAdr:
						found = True
						break
				if not found:
					print("Lost Connexion: "+str(peerAdr)+" player_id: "+str(peersState[peerAdr].player_id.value))
					del(peersState[peerAdr])

			for peer in s.peers:
				#print(str(peer.address)+" "+str(peer.latency))
				if not peer.address in peersState:
					print("New Connexion: "+str(peer.address))
					hello(peer)
					
		time.sleep(0.001)

if __name__ == '__main__':
	main()

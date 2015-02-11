import legume
import time

PORT = 29050

class ServerMessage(legume.messages.BaseMessage):
	STATE_INITIATED=127
	STATE_READY=128
	MessageTypeID = legume.messages.BASE_MESSAGETYPEID_USER+1
	MessageValues = {
		'state' : 'int',
		'player_id' : 'int'}


legume.messages.message_factory.add(ServerMessage)


peersState = {}

def message_handler(sender, message):
	if message.MessageTypeID == ServerMessage.MessageTypeID:
		print(str(sender.address))
		peersState[sender.address].state.value = ServerMessage.STATE_READY

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
					m = ServerMessage()
					m.state.value = ServerMessage.STATE_INITIATED
					m.player_id.value = player_counter
					player_counter += 1
					peersState[peer.address] = m
					print("New Connexion: "+str(peer.address)+" player_id: "+str(m.player_id.value))
				if peersState[peer.address].state.value == ServerMessage.STATE_INITIATED and len(s.peers) == 2:
					peer.send_reliable_message(peersState[peer.address])
					#print("sending to "+str(peer.address)+" state: "+str(peersState[peer.address].state.value)+" player_id: "+str(peersState[peer.address].player_id.value))

		time.sleep(0.001)

if __name__ == '__main__':
	main()

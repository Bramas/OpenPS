# -*- coding:utf8 -*-
import legume
from time import sleep
import time


class ServerCommand(legume.messages.BaseMessage):
	HELLO=128
	CREATE_ROOM=129
	FIND_ROOM=130
	START_GAME=131
	MessageTypeID = legume.messages.BASE_MESSAGETYPEID_USER+1
	MessageValues = {
		'command' : 'int'
		}

legume.messages.message_factory.add(ServerCommand)

class ServerMessage(legume.messages.BaseMessage):
	WHAT_DO_YOU_WANT=128
	IN_ROOM=129
	IN_GAME=130
	MessageTypeID = legume.messages.BASE_MESSAGETYPEID_USER+2
	MessageValues = {
		'state' : 'int',
		'seed' : 'float',
		'room_id' : 'int',
		'player_id' : 'int'}


legume.messages.message_factory.add(ServerMessage)

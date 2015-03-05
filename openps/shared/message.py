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
	NOPE=128
	WHAT_DO_YOU_WANT=129
	IN_ROOM=130
	IN_GAME=131
	MessageTypeID = legume.messages.BASE_MESSAGETYPEID_USER+2
	MessageValues = {
		'state' : 'int',
		'seed' : 'float',
		'room_id' : 'int',
		'player_id' : 'int'}

legume.messages.message_factory.add(ServerMessage)


class PlayerMessage(legume.messages.BaseMessage):
	MessageTypeID = legume.messages.BASE_MESSAGETYPEID_USER+3
	MessageValues = {
		'player_id' : 'int',
		'action' : 'int',
		'target' : 'int'}

legume.messages.message_factory.add(PlayerMessage)
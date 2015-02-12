# -*- coding:utf8 -*-
import legume
from time import sleep
import time


class ServerMessage(legume.messages.BaseMessage):
	STATE_INITIATED=127
	STATE_READY=128
	MessageTypeID = legume.messages.BASE_MESSAGETYPEID_USER+1
	MessageValues = {
		'state' : 'int',
		'player_id' : 'int'}


legume.messages.message_factory.add(ServerMessage)

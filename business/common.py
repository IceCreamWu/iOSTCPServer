# -*- coding:utf-8 –*-
__author__ = 'gzs2477'

from basic import BasicService
from basic import KEY_RESPONSE_CODE

class CommonService(BasicService):

    CID_ECHO = 5200
    CID_ALIVE = 5201

    def __init__(self):
        BasicService.__init__(self)
        self.registerCommand(CommonService.CID_ECHO, self.command_echo)
        self.registerCommand(CommonService.CID_ALIVE, self.command_alive)

    def command_echo(self, requestDict):
        response = {}
        if requestDict.has_key('echoMsg'):
            echoMsg = requestDict['echoMsg']
            response[KEY_RESPONSE_CODE] = 0
            response['echoMsg'] = echoMsg
        else:
            response[KEY_RESPONSE_CODE] = -1
        return response

    def command_alive(self, requestDict):
        response = {}
        response[KEY_RESPONSE_CODE] = 0
        return response
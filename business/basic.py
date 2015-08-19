# -*- coding:utf-8 –*-
__author__ = 'gzs2477'

KEY_SID = 'sid'
KEY_CID = 'cid'
KEY_RESPONSE_CODE = 'responseCode'

TAG_SERVER_ERROR = -1000
TAG_REQUEST_NO_SID = -1001
TAG_REQUEST_NO_CID = -1002
TAG_SERVER_NO_SID = -1003
TAG_SERVER_NO_CID = -1004

class BasicService(object):

    def __init__(self):
        self.commands = {}

    def registerCommand(self, cid, command):
        self.commands[cid] = command;

    def removeCommand(self, cid):
        if self.commands.has_key(cid):
            del self.commands[cid]

    def handleCommand(self, requestDict):
        response = {}
        if requestDict.has_key(KEY_CID):
            cid = requestDict[KEY_CID]
            if self.commands.has_key(cid):
                callback = self.commands[cid]
                response = callback(requestDict)
                response[KEY_CID] = cid
            else:
                response[KEY_RESPONSE_CODE] = TAG_SERVER_NO_CID
                response[KEY_CID] = cid
        else:
            response[KEY_RESPONSE_CODE] = TAG_REQUEST_NO_CID
        return response

class BasicDispatcher(object):

    def __init__(self):
        self.services = {}

    def registerService(self, sid, service):
        self.services[sid] = service

    def removeService(self, sid):
        if self.services.has_key(sid):
            del self.services[sid]

    def handleService(self, requestDict):
        response = {}
        if requestDict.has_key(KEY_SID):
            sid = requestDict[KEY_SID]
            if self.services.has_key(sid):
                service = self.services[sid]
                response = service.handleCommand(requestDict)
                response[KEY_SID] = sid
            else:
                response[KEY_RESPONSE_CODE] = TAG_SERVER_NO_SID
                response[KEY_SID] = sid
        else:
            response[KEY_RESPONSE_CODE] = TAG_REQUEST_NO_SID
        return response
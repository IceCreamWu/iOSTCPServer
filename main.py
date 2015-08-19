# -*- coding:utf-8 –*-

from twisted.protocols.basic import Int32StringReceiver
from twisted.internet import reactor, protocol, endpoints
from config.network import configDispatcher
from business.basic import KEY_RESPONSE_CODE
from business.basic import TAG_SERVER_ERROR
from struct import pack
from traceback import print_exc
import json

class TcpServerProtocol(Int32StringReceiver):

    # 新的连接建立
    def connectionMade(self):
        print 'connectionMade'
        self.dispatcher = configDispatcher()

    # 连接断开
    def connectionLost(self, reason):
        print 'connectionLost:', reason

    # 接收到新的数据
    def stringReceived(self, data):
        try:
            requestDict = json.loads(data);
            responseDict = self.dispatcher.handleService(requestDict)
            response = json.dumps(responseDict)
        except Exception, e:
            print_exc()
            response = {}
            response[KEY_RESPONSE_CODE] = TAG_SERVER_ERROR
        print response
        self.transport.write(pack(">I", len(response)) + response)

class TCPServerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return TcpServerProtocol()

if __name__ == '__main__':
    endpoints.serverFromString(reactor, "tcp:1234").listen(TCPServerFactory())
    reactor.run()
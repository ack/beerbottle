#!/usr/bin/env python
  
port = 9090
  
import os
import sys
import os.path as path
sys.path.append(path.join(path.dirname(__file__), '../gen-py'))
  
import time
  
# Example files
from Users import UserAuthenticator
from Users.ttypes import User, Image
  
# Thrift files
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class Impl(UserAuthenticator.Iface):
    def ping(self, ):
        print 'pong'
        return

    def authenticateUser(self, name, password):
        return User()

    def getUserIcon(self, userId):
        return Image()

    def isValidUser(self, userId):
        return True

    def logoutUser(self, userId):
        return 
    

handler = Impl()
processor = UserAuthenticator.Processor(handler)
transport = TSocket.TServerSocket("0.0.0.0", port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
  
# set server
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)


print 'Starting server (pid:%s) :%s' % (os.getpid(), port)
server.serve()

#!/usr/bin/env python

import sys
import os
import os.path as path
sys.path.append(path.join(path.dirname(__file__), '../gen-py'))

from Users import UserAuthenticator
from Users.ttypes import *
from Users.constants import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol


def t_connect(thrift, host, port):
    try:
        transport = TSocket.TSocket(host, port)
        transport = TTransport.TBufferedTransport(transport)
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        client = thrift.Client(protocol)

        print 'checking...'
        try: print client.transport
        except: pass
        print

        client.transport = transport
        
        transport.open()
        return client
    except Thrift.TException, tx:
        print "%s" % (tx.message)
        raise tx


def main():
    import Users
    client = t_connect(Users.UserAuthenticator, 'localhost', 9090)
    client.ping()
    x = client.authenticateUser('foo', 'bar')
    print x
    client.transport.close()
 
   
main() if __name__ == '__main__' else ''

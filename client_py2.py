#!/usr/bin/env python

import datetime
import time
import sys
import struct
import common_py2 as com2

ADDRESS = '/tmp/usock.sock' 
BUFSIZE = 4096

server = com2.UnixSocket(ADDRESS, BUFSIZE)

def clientMain():
    data = 0
    msg = 0
    while True:
        time.sleep(0.1)
        msg = struct.pack('B',data)
        msg += struct.pack('B',data+1)
        data += 1
        if data >254:
            data = 0
        server.client_send(msg)
        now = datetime.datetime.now()
        print('[client]Send:message={0} [{1}]'.format(msg.encode('hex'), now))

if __name__ == '__main__':
    try:
        clientMain()
    except KeyboardInterrupt:
        print('[client]closed.')
        sys.exit(1)


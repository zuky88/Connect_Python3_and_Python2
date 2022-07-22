#!/usr/bin/env python3

import datetime
import time
import socket
import sys
import os
import common_py3 as com3

ADDRESS = '/tmp/usock.sock'
BUFSIZE = 4096

server = com3.UnixSocket(ADDRESS, BUFSIZE)

def clientMain():
    msg = [0,0]
    data = 0
    while True:
        time.sleep(0.1)
        msg[0] = data
        msg[1] = data + 1
        data += 1
        if data >254:
            data = 0
        server.client_send(msg)
        now = datetime.datetime.now()
        print('[client]Send:message={0} [{1}]'.format(msg, now))

if __name__ == '__main__':
    try:
        clientMain()
    except KeyboardInterrupt:
        print('[client]closed.')
        sys.exit(1)

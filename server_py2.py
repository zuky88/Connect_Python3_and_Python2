#!/usr/bin/env python

import datetime
import sys
import os
import common_py2 as com2

ADDRESS = '/tmp/usock.sock'
BUFSIZE = 4096

server = com2.UnixSocket(ADDRESS, BUFSIZE)
server.check_socketfile()

def serverMain():
    while True:
        msg = server.receive()
        now = str(datetime.datetime.now())
        print("[server]Recv:message={0}[{1}]".format(msg, now))

def start_server():
    server.server_listen()
    now = str(datetime.datetime.now())
    print("[server]Opend socket.(path={0}, size={1})[{2}]".format(server.path, server.size, now))
    print('[server]Waiting access from client.')
    serverMain()

if __name__ == '__main__':
    try:
        start_server()
    except KeyboardInterrupt:
        print('[server]closed.')
        os.remove(ADDRESS)
        sys.exit(1)






#!/usr/bin/env python3

import datetime
import sys
import os
import common_py3 as com3

ADDRESS = '/tmp/usock.sock'
BUFSIZE = 4096

server = com3.UnixSocket(ADDRESS, BUFSIZE)
server.check_socketfile()

def serverMain():
    while True:
        msg = server.receive_from_py2()
        now = str(datetime.datetime.now())
        print("[server]Recv:mssage={0}[{1}]".format(msg, now))

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






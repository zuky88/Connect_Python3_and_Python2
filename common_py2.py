import struct
import socket
import os

class UnixSocket():
    def __init__(self, path, size):
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.path = path
        self.size = size
        self.conn = ''
        self.address = ''
    def check_socketfile(self):
        if os.path.exists(self.path):
            os.remove(self.path)
    def server_listen(self):
        self.s.bind(self.path)
        self.s.listen(1)
    def receive(self):
        int_d = 0
        try:
            self.conn, self.address = self.s.accept()
            recv_d = self.conn.recv(self.size)
            int_d = struct.unpack('BB',recv_d)
        except Exception as e:
            print('>UnixSocket receive error:{0}'.format(e))
        return int_d
    def client_send(self, data):
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            self.s.connect(self.path)
            self.s.send(bytes(data))
        except Exception as e:
            self.s.close()

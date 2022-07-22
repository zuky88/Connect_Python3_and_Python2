import socket
import os

class IntFloat():
    def __init__(self) -> None:
        pass
    def is_int(self, s) -> bool:
        try:
            int(s)
        except ValueError:
            return False
        return True
    def is_float(self, s) -> bool:
        try:
            float(s)
        except ValueError:
            return False
        return True

class Str2Int(IntFloat):
    def __init__(self) -> None:
        super().__init__()
    def strInt2int(self, data:int):
        res = 0
        if  self.is_int(data):
            res = (int(data))
        return res   
    def strFloat10_2int(self, data:str):
        res = 0
        if  self.is_float(data):
            res = (int(float(data) * 10))
        return res   
    def strFloat100_2int(self, data:str):
        res = 0
        if  self.is_float(data):
            res = (int(float(data) * 100))
        return res   
    def strFloat1000_2int(self, data:str):
        res = 0
        if  self.is_float(data):
            res = (int(float(data) * 1000))
        return res   
    def sel2int(self, data:str, sellist:dict):
        res = 0
        for item, n in sellist.items():
            if data == item:
                res = n
        return res

s2i = Str2Int()

class UnixSocket():
    def __init__(self, path, size) -> None:
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
        self.s.listen()
    def receive_from_py2(self) -> int:
        self.conn, self.address = self.s.accept()
        recv_d = self.conn.recv(self.size)
        int_d = []
        for d in recv_d:
            int_d.append(s2i.strInt2int(d))
        return int_d
    def receive_from_py3(self):
        self.conn, self.address = self.s.accept()
        data = self.conn.recv(self.size)
        return data
    def client_send(self, data:list):
        self.s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        try:
            self.s.connect(self.path)
            self.s.send(bytes(data))
        except Exception as e:
            self.s.close()

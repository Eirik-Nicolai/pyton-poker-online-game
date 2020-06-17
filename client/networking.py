import socket

class Helper():
    def __init__(self):
        self._conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server = "192.168.0.4"
        self._port = 555
        self._addr = (self._server, self._port)

    def connect(self):
        try:
            print("connecting...")
            self._conn.connect(self._addr)
            return self._conn.recv(4096).decode()
        except socket.error as e:
            print("error 1 : ", e)

    def send(self, data):
        try:
            self._conn.send(str.encode(data))
            #return self._conn.recv(4096).decode()
        except socket.error as e:
            print("error 2: " + str(e))

    def recv(self):
        try:
            data = self._conn.recv(4096).decode()
            return data
        except socket.timeout:
            pass
        except WindowsError as winerr:
            if winerr.errno == 10035:
                return "TIMEOUT"

    def close(self):
        self._conn.close()

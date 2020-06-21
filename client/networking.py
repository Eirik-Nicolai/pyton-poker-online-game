import socket, json

class Helper():
    def __init__(self):
        self._conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._server = "192.168.0.4"
        self._port = 555
        self._addr = (self._server, self._port)

    def connect(self):
        try:
            self._conn.connect(self._addr)
        except socket.error as e:
            print("error 1 : ", e)

    def check_connection(self):
        data = self.recv()
        if data is not None:
            datal = data.split(';')
            if datal[0] == "CONNECTED":
                self._id = datal[1]
                return self._id
            else:
                return None
        else:
            return None

    def send(self, data):
        try:
            self._conn.send(str.encode(data))
        except socket.error as e:
            print("error 2: " + str(e))

    def recv(self):
        try:
            data = self._conn.recv(4096).decode()
            return data
        except socket.timeout:
            print("timeout")
            return None
        except WindowsError as winerr:
            if winerr.errno == 10035:
                return None

    def close(self):
        pass
        self._conn.close()

class WrapperJson():
    def __init__(self):
        self.header = ""
        self.type   = ""
        self.body   = ""

    def get(self):
        return json.dumps({
                "header" : self.header,
                "type"   : self.type,
                "body"   : self.body
            })

    def recv(self, json):
        recv = json.loads(json)
        self.header = recv["header"]
        self.type   = recv["type"]
        self.body   = recv["body"]


class Message(WrapperJson):
    def __init__(self):
        super().__init__()

    def fold(self):
        self.header = ""
        self.type = "action"
        self.body = {
            "action" : "fold"
        }
        return super().get()

if __name__ == '__main__':
    print("networking")

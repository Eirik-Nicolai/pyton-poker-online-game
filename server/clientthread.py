
import threading, socket
from queue import Queue

from json_wrapper import JsonWrapper
## TODO honestly unnecessary as the server can listen to on and one players
## though would still need thread for thigns like a chat etc
## maybe one for calculating winner?

class Client(threading.Thread):
    def __init__(self, conn, queues):
        threading.Thread.__init__(self)
        print("thread")
        self._conn = conn[0]
        self._addr = conn[1]
        self._q = queues
        self._run = True

    def run(self):
        confirmation = "CONNECTED;"+str(self._addr[0])+","+str(self._addr[1])
        self._conn.send(confirmation.encode())
        print("[", self._addr, " connected]")
        self._q[1].put("connected")
        while self._run:
            if not self._q[0].empty():
                for i in range(self._q[0].qsize()):
                    qdata = self._q[0].get()
                    type = qdata["header"]
                    if type == "listening":
                        self._conn.send(b"listening")
                    elif type == "connected":
                        self._conn.send(JsonWrapper().tojson(qdata).encode())
                    else:
                        print("E: qdata not defined : ", qdata)
                    self._q[0].task_done()

            try:
                data = None
                try:
                    data = self._conn.recv(4096).decode()
                except socket.timeout:
                    print("timeout")
                    continue
                except WindowsError as winerr:
                    if winerr.errno == 10035:
                        continue

                if data is None:
                    print("something happened with the client, disconnecting")
                    break

                json = JsonWrapper().fromjson(data)
                if json is None:
                    if data != "break": continue

                if data == "break":
                    break
                type = json["type"]
                if type == "listening":
                    self._q[0].p({"header" : "listening"})
                elif type == "hello" and self._q[1].empty():
                    print("recvd from " + str(self._addr))
                    self._q[1].put("hello")
            except socket.error as e:
                print("error 3 ", e)
                break

        #game_running = True
        #while game_running:
            #break
        self._run = False
        print("Terminating connection with " + str(self._addr))

        self._conn.close()


    def queue(self):
        return self._q[0]

    def close_connection(self):
            print("closing " + str(self._addr))
            self._run = False

if __name__ == '__main__':
    print("threadmain")

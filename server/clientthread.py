
import threading, socket
from queue import Queue

## TODO honestly unnecessary as the server can listen to on and one players
## though would still need thread for thigns like a chat etc
## maybe one for calculating winner?

class Client(threading.Thread):
    def __init__(self, conn, queues):
        threading.Thread.__init__(self)
        self._conn = conn[0]
        self._addr = conn[1]
        self._q = queues
        self._run = False

    def run(self):
        self._conn.send(b"CONNECTED")
        self._run = True
        while self._run:
            try:
                data = self._conn.recv(4096).decode()

                if data == "break":
                    break
                if data is not None:
                    if data == "listening":
                        self._conn.send(b"S: listening")
                    elif data == "hello" and self._q[1].empty():
                        print("recvd from " + str(self._addr))
                        self._q[1].put("hello")
                    elif "RGB" in data:
                        var = self._q[0].get()
                        dataL = data.split(":")
                        strbg = dataL[1].split(";")
                        bg = [int(numeric_string) for numeric_string in strbg]
                        if dataL[0] == "P":
                            bg[0] += 2
                            bg[1] += 2
                            bg[2] += 2
                        else:
                            bg[0] -= 2
                            bg[1] -= 2
                            bg[2] -= 2
                        var = bg
                        self._q[0].put(var)
                        answr = str(var[0])+";"+str(var[1])+";"+str(var[2])
                        self._conn.send(answr.encode())
            except socket.error as e:
                print("error 3 ", e)
                break

        #game_running = True
        #while game_running:
            #break

        print("Terminating connection with " + str(self._addr))

        self._conn.close()

    def close_connection(self):
            print("closing " + str(self._addr))
            self._run = False

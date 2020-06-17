
import threading, socket
from queue import Queue

class Master(threading.Thread):
    def __init__(self, socket, queue):
        threading.Thread.__init__(self)
        self._client_threads = []
        self._socket = socket
        self._q = queue
        self._run = False

    def run(self):
        print("Running master")
        self._run = True
        while self._run:
            if not self._q.empty():
                queue_data = self._q.get()
                if queue_data == "hello":
                    for conn, thread in self._client_threads:
                        print("sending to " + str(thread._addr))
                        conn.sendto(b"S: Hi!", thread._addr)

                    print("queuesize: " + str(self._q.qsize()))

        #game_running = True
        #while game_running:
            #break

        print("Terminating connection with " + str(self._addr))

        for thread in self._client_threads:
            self._socket.close_connection()

        self._socket.close()

    def add_thread(self, conn, thread):
        self._client_threads.append((conn, thread))

    def close_connection(self):
            print("closing " + str(self._addr))
            self._run = False


import threading, socket
from queue import Queue

from game import Game
from player import Player

class Master(threading.Thread):
    def __init__(self, socket, queue):
        threading.Thread.__init__(self)
        self._client_threads = {}
        self._socket = socket
        self._q = queue
        self._run = False
        self._game = Game()

    def run(self):
        print("Running master")
        self._run = True
        while self._run:
            if len(self._client_threads) > 0:
                id = []
                for addr, thread in self._client_threads.items():
                    if thread._run == False:
                        print("ending thread for ", addr)
                        id.append(addr)
                for addr in id:
                    del self._client_threads[addr]
                    del self._game._players[str(addr)]

            if not self._q.empty():
                for i in range(self._q.qsize()):
                    qdata = self._q.get()
                    if qdata == "hello":
                        for conn, thread in self._client_threads:
                            conn.sendto(b"S: Hi!", thread._addr)
                    elif qdata == "connected":
                        answr = {
                            "header" : "connected",
                            "type"   : "player_connect",
                            "body"   : []
                            }
                        for id, player in self._game._players.items():
                            p = {"id" : id, "name" : player._name}
                            answr["body"].append(p)
                        for addr, thread in self._client_threads.items():
                            thread.queue().put(answr)
                    self._q.task_done()

        #game_running = True
        #while game_running:
            #break

        print("Terminating connection with " + str(self._addr))

        for thread in self._client_threads:
            self._socket.close_connection()

        self._socket.close()

    def add_thread(self, addr, thread):
        self._client_threads[addr] = thread
        self._game.add_player(str(addr))


    def close_connection(self):
            print("closing " + str(self._addr))
            self._run = False



if __name__ == '__main__':
    print("threadmaster")

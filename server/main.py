import socket
import sys
import threading
from queue import Queue
from player import Player
from clientthread import Client
from masterthread import Master

players = {
    #(ip, host) : player_class
}


server = "192.168.0.4"
port = 555
print("set up server")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

try:
    print("Binding socket on ip " + server + " and port " + str(port))
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen()
print("Listening...")


if __name__ == "__main__":
    ##init some things ?
    masterqueue = Queue()
    queue = Queue()

    masterthread = Master(s, masterqueue)
    masterthread.start()

    menu = True
    while menu:
#        try:
        conn, addr = s.accept()
        conn.setblocking(0)
        print("Connected to ", addr)
        new_thread = Client((conn, addr), [queue, masterqueue])
        masterthread.add_thread(addr, new_thread)

        new_thread.start()

        #except KeyboardInterrupt:
        #    for id, thread in threads:
        #        thread.close_connection()
        #finally:
        #    sys.exit()

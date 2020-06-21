import socket

conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "192.168.0.4"
port = 555
addr = (server, port)


conn.connect(addr)

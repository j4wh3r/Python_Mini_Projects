import socket

host = "127.0.0.1"
port = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    s.sendall(b'hello world')
    data = s.recv(1024)
print('received', repr(data))
import socket

host = "127.0.0.1"
port = 9000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)
    print("server started ! waiting for connections...")
    connection,address = s.accept()
    print("client connected with address",address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    connection.sendall(b' --Message received-- \n')
    d = data.decode('utf-8')
    print(d)
connection.close()


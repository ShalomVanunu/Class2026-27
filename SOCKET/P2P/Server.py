import socket

IP = "172.20.130.55"
PORT = 6000 # 1-65500 (1-1024 Well knwn port)

Server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # AF_INET- IPv4 , TCP

Server_socket.bind((IP,PORT))

Server_socket.listen()

Client_obj, Client_IP = Server_socket.accept()

print(Client_IP)
print(Client_obj.recv(1024).decode())





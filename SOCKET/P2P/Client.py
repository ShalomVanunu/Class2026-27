import socket


IP = "172.20.130.55"#
PORT = 6000 # 1-65500 (1-1024 Well knwn port)

Client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Client_socket.connect((IP,PORT))

Client_socket.send("Hello".encode())
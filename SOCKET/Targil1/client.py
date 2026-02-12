import socket


IP_SERVER = "172.20.130.55"
PORT = 5500


Client_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client_obj.connect((IP_SERVER,PORT))

print("Connected to Server")

while True:
    data_send = input(" Write a Message [bye to end session] : ")
    if data_send.lower() == "bye" :
        Client_obj.close()
        break
    Client_obj.send(data_send.encode())
    data_received = Client_obj.recv(1024).decode()
    if data_received.lower() == "bye":
        Client_obj.close()
        break
    print(f" Message from Server : {data_received}")



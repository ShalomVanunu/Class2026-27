import socket

IP_SERVER = "172.20.130.55"
PORT = 5500


Server_Obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Server_Obj.bind((IP_SERVER,PORT))
print(f" The Server listen on IP  {IP_SERVER}  & PORT {PORT}")

Server_Obj.listen()
print(" The Server is Waiting for Client.....")

Client_obj, IP_Port = Server_Obj.accept()
print(f" Client has connected on {IP_Port}")

while True:
    data_received = Client_obj.recv(1204).decode()
    if data_received.lower() == "bye":
        Client_obj.close()
        break
    print(f" Message from Client : {data_received}")
    data_send = input(" Write a Message :")
    if data_send.lower() == "bye":
        Client_obj.close()
        break
    Client_obj.send(data_send.encode())







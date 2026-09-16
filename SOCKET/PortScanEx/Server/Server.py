import socket
import DbHandle

IP = "172.20.138.211"
PORT = 5555

def main():
    Server_Soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    Server_Soc.bind((IP,PORT))
    Server_Soc.listen()
    print(" Server Waiting Client to connect...")
    Client_soc, IP_Port = Server_Soc.accept()
    print(f" client connected ...{IP_Port}")

    while True:
        choose = input(""" Choose :
         1. Start Scan
         2. Exit \n""")
        if int(choose) == 2:
            Client_soc.send("bye".encode())
            print("Bye")
            break
        Client_soc.send("start".encode())
        data = Client_soc.recv(1024).decode()
        print(f"{IP_Port[0]}: Open Ports {data}")
        DbHandle.save_to_db(IP_Port[0],data)

main()
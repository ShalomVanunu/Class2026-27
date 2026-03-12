import socket



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
         1 .Start Scan
         2. Exit \n""")
        if int(choose) == 2:
            Client_soc.send("bye".encode())
            print("Bye")
            break
        Client_soc.send("start".encode())




main()
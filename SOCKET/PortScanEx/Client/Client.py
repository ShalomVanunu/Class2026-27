import PortScan
import socket

IP = "172.20.138.211"
PORT = 5555

Client_soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
Client_soc.connect((IP,PORT))
print(" client Connected...")

while True:
    data = Client_soc.recv(1024).decode()
    if data == "bye":
        break
    if data== "start":
        list_ports = PortScan.portscan(IP)
        print(list_ports)



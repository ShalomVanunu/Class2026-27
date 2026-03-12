import socket
import datetime
import threading


def portscan(target):
    print("Target IP:", target)
    open_port_list =[]
    for port in range(1, 500):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)
        result = sock.connect_ex((target,port))
        if result == 0:
            #print("Port" ,port,"is open")
            open_port_list.append(port)
        sock.close()
    return open_port_list



import os
def Get_IP():
    ip1=os.popen("ipconfig").read().strip().split("\n")
    print(ip1)
    print(ip1[7].split(":")[1].strip())

Get_IP()
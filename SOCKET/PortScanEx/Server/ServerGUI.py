import socket
import DbHandle
import tkinter as tk

IP = "172.20.138.211"
PORT = 5555


root = tk.Tk()
root.title("Port Scan GUI")
root.geometry("600x450")

Server_Soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Server_Soc.bind((IP, PORT))
Server_Soc.listen()
print(" Server Waiting Client to connect...")
Client_soc, IP_Port = Server_Soc.accept()
print(f" client connected ...{IP_Port}")



def start_scan():
    Client_soc.send("start".encode())
    data = Client_soc.recv(1024).decode() # get the list data
    text.insert(tk.END, IP_Port[0]+": "+data) #show the data on Text Window
    DbHandle.save_to_db(IP_Port[0], data) #save DB

def exit_scan():
    Client_soc.send("bye".encode())
    root.destroy() #kill the window



start = tk.Button(root, text="Start Scan", command=start_scan)
start.pack()

exit = tk.Button(root, text="Exit", command=exit_scan)
exit.pack()

text = tk.Text(root, height=200 , width=400)
text.pack()

root.mainloop()


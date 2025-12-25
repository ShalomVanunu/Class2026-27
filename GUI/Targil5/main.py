import tkinter as  tk
import DBhandle
import HASHMD5
DBfile= "users.db"

app = tk.Tk()
app.title("Login")
app.geometry("500x500")

label1 = tk.Label(app, text="Login Page",font=("Ariel", 40))
label1.pack()
label2 = tk.Label(app, text="Username")
label2.pack()
entry1 = tk.Entry(app)
entry1.pack()
label3 = tk.Label(app, text="Password")
label3.pack()
entry2 = tk.Entry(app, show="*")
entry2.pack()

def verify_data():
    username = entry1.get()
    password = entry2.get()
    SQL_SELECT = f"SELECT password FROM users WHERE username = '{username}' "
    data = DBhandle.read_db(DBfile,SQL_SELECT)
    hash_password = data[0][0]
    if hash_password == HASHMD5.hash(password):
        app.destroy()
        app1 = tk.Tk()
        app1.title("Search")
        app1.geometry("500x500")
    else:
        label4.config(text = "Wrong Password")





button1 = tk.Button(app, text="Submit", command=verify_data)
button1.pack()
label4 = tk.Label(app, text="")
label4.pack()

app.mainloop()
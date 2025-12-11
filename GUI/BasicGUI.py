import tkinter as  tk

app = tk.Tk()
app.title("ShalomGUI")
app.geometry("500x500")

label1 = tk.Label(app, text=" Welcome Class",font=("Ariel", 40))
label1.pack()
label2 = tk.Label(app, text="Name")
label2.pack()
entry1 = tk.Entry(app)
entry1.pack()

def do_something():
   label3.configure(text=entry1.get(), font=("Ariel",20))
   text1.insert(tk.END,entry1.get())
def delete():
    label3.configure(text="")


button1 = tk.Button(app, text="Submit", command=do_something)
button1.pack()
button2 = tk.Button(app, text="Delete", command=delete)
button2.pack()
label3 = tk.Label(app, text="")
label3.pack()

text1 = tk.Text(app, width=40, height=60)
text1.pack()

app.mainloop()
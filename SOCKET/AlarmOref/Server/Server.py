import socket
import threading
import tkinter as tk
from tkinter import ttk
import handleDB

# [span_6](start_span)[span_7](start_span)הגדרות חיבור[span_6](end_span)[span_7](end_span)
IP = "127.0.0.1"
PORT = 9999


def handle_client(client_soc):
    # [span_8](start_span)קבלת נתוני ההתראה מהלקוח[span_8](end_span)
    data = client_soc.recv(1024).decode()
    if data:
        import json
        alert = json.loads(data)

        # שמירה למסד הנתונים בעזרת הקובץ השני
        handleDB.save_alert(alert['id'], alert['time'], alert['category'], alert['title'], alert['areas'])

        # [span_9](start_span)שליחת אישור חזרה ללקוח[span_9](end_span)
        client_soc.send("ACK".encode())
    client_soc.close()


def socket_server():
    server = socket.socket()
    server.bind((IP, PORT))
    server.listen(5)
    while True:
        client_soc, addr = server.accept()
        # [span_10](start_span)הפעלת Thread כדי שהשרת ימשיך להאזין גם כשהחלון פתוח[span_10](end_span)
        threading.Thread(target=handle_client, args=(client_soc,)).start()


# [span_11](start_span)פונקציה לכפתור "ייבא התראות"[span_11](end_span)
def load_from_db():
    # ניקוי הטבלה לפני טעינה
    for i in tree.get_children():
        tree.delete(i)

    import sqlite3
    conn = sqlite3.connect('oref_alerts.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts")
    rows = cursor.fetchall()
    # מעדכן את הכיתוב של המונה לפי כמות השורות שנמצאו
    lbl_count.config(text=f"מספר התראות: {len(rows)}")

    for row in rows:
        tree.insert("", "end", values=row)

    [span_12](start_span)
    lbl_count.config(text=f"מספר התראות: {len(rows)}")  # עדכון המונה[span_12](end_span)
    conn.close()


# [span_13](start_span)[span_14](start_span)יצירת ממשק Tkinter[span_13](end_span)[span_14](end_span)
root = tk.Tk()
root.title("שרת פיקוד העורף")

lbl_count = tk.Label(root, text="מספר התראות: 0")
lbl_count.pack()

tree = ttk.Treeview(root, columns=("ID", "שעה", "קטגוריה", "כותרת", "אזורים"), show='headings')
for col in ("ID", "שעה", "קטגוריה", "כותרת", "אזורים"):
    tree.heading(col, text=col)
tree.pack()

btn = tk.Button(root, text="ייבא התראות", command=load_from_db)
btn.pack()

# הרצת השרת ברקע
threading.Thread(target=socket_server, daemon=True).start()

root.mainloop()
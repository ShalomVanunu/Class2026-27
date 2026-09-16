import sqlite3

def save_alert(alert_id, alert_time, category, title, areas):
    # חיבור למסד הנתונים של פיקוד העורף
    conn = sqlite3.connect('oref_alerts.db')
    cursor = conn.cursor()

    # [span_0](start_span)יצירת הטבלה לפי הדרישות במשימה[span_0](end_span)
    cursor.execute('''CREATE TABLE IF NOT EXISTS alerts 
                      (id TEXT PRIMARY KEY, time TEXT, category TEXT, title TEXT, areas TEXT)''')

    try:
        # [span_1](start_span)[span_2](start_span)הכנסת הנתונים לטבלה[span_1](end_span)[span_2](end_span)
        cursor.execute("INSERT INTO alerts VALUES (?, ?, ?, ?, ?)",
                       (alert_id, alert_time, category, title, areas))
        conn.commit()
        print("--- Alert saved to Database! ---")
    except:
        # [span_3](start_span)אם ה-ID כבר קיים, זה לא יכניס שוב (מניעת כפילות)[span_3](end_span)
        print("--- Alert already exists ---")

    conn.close()

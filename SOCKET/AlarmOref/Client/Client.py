import socket
import requests
import time
import json
from datetime import datetime

# הגדרות לפי המשימה
OREF_URL = "http://127.0.0.1:8080/WarningMessages/alert/alerts.json"
SERVER_IP = "127.0.0.1"
SERVER_PORT = 9999

# טבלת קטגוריות מההוראות
CAT_MAP = {
    "1": "ירי רקטות וטילים",
    "2": "כלי טיס עוין",
    "3": "רעידת אדמה",
    "4": "חומרים מסוכנים",
    "5": "צונאמי",
    "6": "חדירת כלי טיס עוין",
    "171": "טיל בלתי קונבנציונלי",
    "13": "אירוע רדיולוגי"
}

last_id = ""  # שומרת את ה-ID האחרון כדי למנוע כפילויות

print("הלקוח התחיל לעבוד...")

while True:
    try:
        # דוגמת את ה-API של פיקוד העורף
        response = requests.get(OREF_URL, timeout=5)

        # בודקת אם יש התראה והיא לא ריקה
        if response.status_code == 200 and response.text.strip():
            data = response.json()
            alert_id = data.get("id")

            # שולחת רק אם זו התראה חדשה
            if alert_id != last_id:
                last_id = alert_id

                # מעבדת את הנתונים לפי מה שביקשו במשימה
                category_name = CAT_MAP.get(data.get("cat"), "אחר")
                current_time = datetime.now().strftime("%H:%M:%S")
                areas_str = ", ".join(data.get("data", []))

                # מסדרת את ההתראה למשלוח
                alert_packet = {
                    "id": alert_id,
                    "time": current_time,
                    "category": category_name,
                    "title": data.get("title"),
                    "areas": areas_str
                }

                # מתחברת לשרת ושולחת את ה-JSON
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.connect((SERVER_IP, SERVER_PORT))
                    s.sendall(json.dumps(alert_packet).encode('utf-8'))

                    # מקבלת אישור מהשרת
                    ack = s.recv(1024).decode()
                    if ack == "ACK":
                        print(f"התראה נשלחה בהצלחה: {alert_id}")

    except Exception as e:
        # אם יש בעיה בחיבור פשוט מדפיסה ומנסה שוב
        print("מנסה להתחבר לסימולטור או לשרת...")

    time.sleep(3)  # דוגמת כל 3 שניות לפי

"""
╔══════════════════════════════════════════════════════════════╗
║   oref_simulator.py – סימולטור API פיקוד העורף              ║
║   מדמה את: /WarningMessages/alert/alerts.json               ║
╚══════════════════════════════════════════════════════════════╝

התקנה:
    pip install flask

הרצה:
    python oref_simulator.py

כתובת:
    http://127.0.0.1:8080/WarningMessages/alert/alerts.json
"""

import json
import random
import time
import threading
from flask import Flask, jsonify, Response
from datetime import datetime

app = Flask(__name__)

# ──────────────────────────────────────────────────────────────
#  בנק נתונים לסימולציה
# ──────────────────────────────────────────────────────────────

CATEGORIES = {
    "1":  "ירי רקטות וטילים",
    "2":  "כלי טיס עוין",
    "6":  "חדירת כלי טיס עוין",
    "7":  "טיל בלתי קונבנציונלי",
}

DESCRIPTIONS = {
    "1":  "היכנסו למרחב המוגן",
    "2":  "היכנסו דיימ למרחב המוגן",
    "6":  "היכנסו דיימ למרחב המוגן",
    "7":  "היכנסו למרחב המוגן",
}

AREAS_BANK = [
    "גורנות הגליל", "קריית שמונה", "נהריה", "עכו",
    "חיפה", "תל אביב - יפו", "אשדוד", "אשקלון",
    "באר שבע", "שדרות", "נתיבות", "אופקים",
    "ירושלים", "רמת גן", "פתח תקווה", "ראשון לציון",
    "חולון", "בת ים", "רחובות", "נס ציונה",
    "מטולה", "כרמיאל", "צפת", "טבריה",
    "עפולה", "נצרת עילית", "חדרה", "נתניה",
    "הרצליה", "רעננה", "כפר סבא", "פתח תקווה",
]

# ──────────────────────────────────────────────────────────────
#  מצב הסימולטור (משתנה לאורך הזמן)
# ──────────────────────────────────────────────────────────────

class SimulatorState:
    def __init__(self):
        self.active_alert   = None   # ההתראה הנוכחית (None = שקט)
        self.alert_end_time = 0      # מתי ההתראה מסתיימת
        self.lock           = threading.Lock()

    def generate_alert(self):
        """יצירת התראה רנדומלית."""
        cat     = random.choice(list(CATEGORIES.keys()))
        areas   = random.sample(AREAS_BANK, k=random.randint(1, 5))
        alert_id = str(int(time.time() * 1000)) + "00000"

        return {
            "id":    alert_id,
            "cat":   cat,
            "title": CATEGORIES[cat],
            "data":  areas,
            "desc":  DESCRIPTIONS[cat],
        }

    def update(self):
        """
        עדכון מצב הסימולטור:
        - 30% סיכוי ל'פתיחת' התראה חדשה כל מחזור
        - ההתראה נמשכת 8-20 שניות
        - אחרי הזמן – חוזרים למצב שקט (JSON ריק)
        """
        with self.lock:
            now = time.time()

            if self.active_alert and now < self.alert_end_time:
                # התראה פעילה – לא משנים
                return

            if now >= self.alert_end_time:
                # ההתראה הסתיימה
                if self.active_alert:
                    print(f"[SIM] ✅ שקט – ההתראה {self.active_alert['id'][:12]}... הסתיימה")
                self.active_alert = None

            # הגרלה: האם להפעיל התראה חדשה?
            if not self.active_alert and random.random() < 0.35:
                self.active_alert   = self.generate_alert()
                duration            = random.randint(8, 20)
                self.alert_end_time = now + duration
                cat  = self.active_alert["cat"]
                areas = ", ".join(self.active_alert["data"])
                print(f"[SIM] 🔔 התראה חדשה! ({CATEGORIES[cat]}) | {areas} | {duration}s")

    def get_response(self):
        """מחזיר את ה-JSON הנוכחי לשליחה ללקוח."""
        with self.lock:
            if self.active_alert:
                return self.active_alert
            return None   # אין התראות – מחזיר ריק


state = SimulatorState()


# ──────────────────────────────────────────────────────────────
#  Thread עדכון רקע (כל שנייה)
# ──────────────────────────────────────────────────────────────

def background_loop():
    while True:
        state.update()
        time.sleep(1)

bg = threading.Thread(target=background_loop, daemon=True)
bg.start()


# ──────────────────────────────────────────────────────────────
#  Routes
# ──────────────────────────────────────────────────────────────

@app.route("/WarningMessages/alert/alerts.json")
def alerts():
    """
    נקודת הקצה הראשית – מדמה את ה-API של פיקוד העורף.
    מחזיר JSON של ההתראה הפעילה, או תגובה ריקה אם אין התראה.
    """
    alert = state.get_response()

    if alert:
        resp = Response(
            json.dumps(alert, ensure_ascii=False),
            status=200,
            mimetype="application/json"
        )
    else:
        # ה-API האמיתי מחזיר מחרוזת ריקה כשאין התראות
        resp = Response("", status=200, mimetype="application/json")

    # כותרות CORS (כדי שלקוחות מדפדפן יוכלו לגשת)
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Cache-Control"]               = "no-cache"
    return resp


@app.route("/status")
def status():
    """דף סטטוס – מציג מה קורה בסימולטור כרגע."""
    alert = state.get_response()
    remaining = max(0, int(state.alert_end_time - time.time()))

    return jsonify({
        "simulator": "oref-api-simulator",
        "time":      datetime.now().strftime("%H:%M:%S"),
        "active":    alert is not None,
        "alert":     alert,
        "remaining_seconds": remaining if alert else 0,
        "endpoints": {
            "alerts": "/WarningMessages/alert/alerts.json",
            "status": "/status",
            "trigger": "POST /trigger?cat=1&areas=תל אביב,חיפה",
        }
    })


@app.route("/trigger", methods=["POST", "GET"])
def trigger():
    """
    הפעלת התראה ידנית לבדיקה.
    שימוש: POST /trigger?cat=1&areas=תל אביב,חיפה&duration=15
    """
    from flask import request

    cat      = request.args.get("cat", "1")
    areas    = request.args.get("areas", "תל אביב")
    duration = int(request.args.get("duration", 15))

    if cat not in CATEGORIES:
        return jsonify({"error": f"קטגוריה לא קיימת. אפשרויות: {list(CATEGORIES.keys())}"}), 400

    areas_list = [a.strip() for a in areas.split(",")]
    alert_id   = str(int(time.time() * 1000)) + "00000"

    with state.lock:
        state.active_alert = {
            "id":    alert_id,
            "cat":   cat,
            "title": CATEGORIES[cat],
            "data":  areas_list,
            "desc":  DESCRIPTIONS[cat],
        }
        state.alert_end_time = time.time() + duration

    print(f"[SIM] ⚡ התראה ידנית הופעלה! ({CATEGORIES[cat]}) | {areas} | {duration}s")

    return jsonify({
        "status":   "triggered",
        "alert":    state.active_alert,
        "duration": duration,
    })


@app.route("/clear", methods=["POST", "GET"])
def clear():
    """ניקוי ידני של ההתראה הפעילה."""
    with state.lock:
        state.active_alert   = None
        state.alert_end_time = 0
    print("[SIM] 🧹 התראה נוקתה ידנית")
    return jsonify({"status": "cleared"})


# ──────────────────────────────────────────────────────────────
#  הפעלה
# ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("=" * 55)
    print("  🛡  סימולטור API פיקוד העורף")
    print("=" * 55)
    print(f"  API:     http://127.0.0.1:8080/WarningMessages/alert/alerts.json")
    print(f"  סטטוס:   http://127.0.0.1:8080/status")
    print(f"  הפעלה:   http://127.0.0.1:8080/trigger?cat=1&areas=תל אביב,חיפה")
    print(f"  ניקוי:   http://127.0.0.1:8080/clear")
    print("=" * 55)
    print("  התראות אוטומטיות מופעלות כל ~10 שניות (35% הסתברות)")
    print("=" * 55)
    print()

    app.run(host="0.0.0.0", port=8080, debug=False)

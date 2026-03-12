import tkinter as tk


# --- פונקציות (הלוגיקה של המערכת) ---

def show_text():
    # קבלת הטקסט מתיבת הקלט
    content = my_entry.get()

    # משימה 3: בוקר טוב - הוספת המילים לפני הטקסט
    new_message = "הודעה חדשה: " + content

    # עדכון הטקסט בחלונית הלבנה
    result_label.config(text=new_message)

    # משימה 4: אתגר (סייבר) - ספירת תווים ועדכון התווית
    char_count = len(content)  # הפונקציה len סופרת את כמות התווים
    count_label.config(text=f"מספר תווים שהוקלדו: {char_count}")


# משימה 1: הכל מהתחלה (Reset) - פונקציה לניקוי המסך
def clear_all():
    # מחיקת התוכן מתיבת הקלט
    my_entry.delete(0, tk.END)
    # איפוס החלונית הלבנה
    result_label.config(text="")
    # איפוס ספירת התווים (אופציונלי אבל מומלץ)
    count_label.config(text="")


# --- בניית החלון והרכיבים ---

root = tk.Tk()
root.title('מערכת קלט - סייבר מקיף ח"')
root.geometry("400x500")

# 1. תיבת קלט
my_entry = tk.Entry(root, width=30)
my_entry.pack(pady=20)

# 2. כפתור ראשי
# משימה 2: עיצוב - צביעת רקע הכפתור לצהוב (bg="yellow")
my_button = tk.Button(root, text="הצג בחלונית הלבנה", bg="yellow", command=show_text)
my_button.pack(pady=10)

# כפתור ניקוי (חלק ממשימה 1)
clear_button = tk.Button(root, text="נקה", command=clear_all)
clear_button.pack(pady=5)

# 3. חלונית תצוגה לבנה
# משימה 2: עיצוב - צביעת הטקסט לכחול (fg="blue")
result_label = tk.Label(root, text="", bg="white", fg="blue", width=35, height=5)
result_label.pack(pady=20)

# 4. תווית לספירת תווים (חלק ממשימה 4)
count_label = tk.Label(root, text="")
count_label.pack(pady=10)

# פקודה שמשאירה את החלון פתוח
root.mainloop()
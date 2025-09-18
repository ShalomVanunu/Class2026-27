
count = 10

def increment_count_with_global():
    global count # מציין שאנו מתייחסים למשתנה הגלובלי 'count'
    count = count + 1 # משנה את ערכו של המשתנה הגלובלי

def increment_count_without_global():
    # בלי global, פייתון ינסה ליצור משתנה מקומי בשם count
    # ויקבל שגיאה כאשר ננסה להשתמש בו.
    count = count + 1

# הפעלת הפונקציה הראשונה
increment_count_with_global()
#increment_count_without_global()
print(f"הערך של count לאחר השינוי: {count}") # פלט: 11
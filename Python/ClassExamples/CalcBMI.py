def calculate_bmi(weight, height):
    return weight / (height ** 2)

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "תת-משקל"
    elif 18.5 <= bmi < 25:
        return "משקל תקין"
    elif 25 <= bmi < 30:
        return "עודף משקל"
    else:
        return "השמנה"

print("ברוכים הבאים למחשבון BMI!")

weight = float(input("אנא הכנס את משקלך בקילוגרמים: "))
height = float(input("אנא הכנס את גובהך במטרים: "))

bmi = calculate_bmi(weight, height)
category = interpret_bmi(bmi)

print(f"\nה-BMI שלך הוא: {bmi:.2f}")
print(f"קטגוריה: {category}")
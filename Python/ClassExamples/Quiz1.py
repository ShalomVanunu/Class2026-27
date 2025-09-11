healthy_foods = [
    "ברוקולי :34 קלוריות",
    "תרד :25 קלוריות",
    "עגבניות :18 קלוריות",
    "מלפפונים :16 קלוריות",
]

calorie_counter =0
for food in healthy_foods:
    print(food.split(":")[0])
    calorie = food.split(":")[1].split(' ')[0]
    calorie_counter += int(calorie)

print(calorie_counter)

name = input("What is your friut? ")


for food in healthy_foods:
    if name in food.split(":")[0].strip():
        print("food is in the list")


print(" Calc BMI")

height = int(input("enter your height :"))
weight = int(input("enter your weight :"))
BMI = weight/(height**2)
print(f"your BMI is {BMI}")

if BMI<18.5 :
    print("Low weight")
elif 24.9<BMI<18.5:
    print("Good weight")
else:
    print("over weight")


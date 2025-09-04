
names = ["Jessy","Hila","Liel","Lihi","Zohar"]

print(type(names))
print(names)
print(len(names))
names.append("Noa")
print(names)

for name in names:
    print(name)

# sum the numbers in list
numbers = [1,6,5,2,5,9]
sum =0
for number in numbers:
    sum+=number
print(sum)



asked_name = input("enter your name :")
if asked_name in names:
    print(f" the name {asked_name}is on the list")

for name in names :
    if name ==asked_name:
        print("is there")
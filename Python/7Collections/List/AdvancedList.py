import random

names = ["Jessy","Hila","Liel","Lihi","Zohar"]

print(random.choice(names))

print(names[1:])

Hila_index = names.index("Hila")
names[Hila_index] = "Keren"
print(names)

print(names.count("Keren"))

names.remove("Keren")
print(names)


file = open(r"newnames", "w")
file.write("shalom")

with open("newnames", "a") as file:
    file.write("oded")

with open("newnames", "r") as file:
    print(file.read())
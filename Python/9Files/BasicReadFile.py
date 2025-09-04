

file  = open("names.txt", "r") # w - new file each time || a- append

#names = file.read()
names = file.readlines()
print(names)
for name in names:
    print(name)
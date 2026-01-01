import os


os.mkdir("ShalomV.py1") # make directory
path = os.getcwd()
print(path.split("\\"))



os.chdir(r"C:\Users\ShalomV\PycharmProjects\Class2026-27") # change directory

with open("Hello.txt", "w") as file: # create file
    file.write("Helloo class")

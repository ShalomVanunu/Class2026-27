import os

try:
    os.mkdir("OS")
except:
    pass

    os.chdir("OS")
    os.mkdir("Products")
    print(os.getcwd())


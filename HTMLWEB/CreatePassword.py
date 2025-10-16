import random
import string


def write_to_file(password):
    #file_obj = open("passwords.txt", "a")
    #file_obj.write(password)
    #file_obj.close()
    with open("passwords.txt","a") as file:
        file.write(password+"\n")


def create_pass():
    password =""
    password = random.choice(string.ascii_uppercase)
    for _ in range(4):
        password+=random.choice(string.ascii_lowercase)
    password += random.choice(string.punctuation)
    return password

def main():
    for _ in range(10):
        write_to_file(create_pass())


main()





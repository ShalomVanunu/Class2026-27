
secret_password = 'Home2020'

password = input("Enter you Password :")

while password != secret_password :
    password = input("Enter you Password :")
    if password != secret_password :
        continue
    else:
        print("Success")
        break


while True:
    pass_suugest = input("Enter your password")
    if pass_suugest != secret_password:
        continue
    else:
        print("Success")
        break
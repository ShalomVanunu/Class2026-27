
def check(phone,name,id):
    global Flag
    if (phone[:2] == '05' and len(phone)==10 and
        name.islower() and id.isdigit() and len(id)==8):
        print("Data OK")
        Flag=False
    return Flag

Flag = True
while Flag :
    phone = input("Phone :")
    name = input("Name :")
    test = input("ID :")
    check(phone,name,test)
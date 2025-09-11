

def order_names(list_names):
    print(sorted(list_names, reverse=True))
    print(list_names)


#['Alin', 'Talya', 'Topaz', 'Gaya']





list_names = []
while True:
    name = input("What is your friend's name? ")
    if name == "bye":
        break
    list_names.append(name)

order_names(list_names)




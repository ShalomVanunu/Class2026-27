

def function_name(num1,num2):
    sum = int(num1) + int(num2)
    return sum


while True:

    num1= input("Enter num1 [type exit to end]")
    num2= input("Enter num2 [type exit to end]")
    if num1 == "exit" or num2 == "exit":
        break
    sum = function_name(num1,num2)
    print(sum)






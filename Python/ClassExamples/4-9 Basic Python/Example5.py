

name  = input('Enter your name: ')
char = input('Enter your char: ')

if char in name:
    print(f'{char} is in {name}')
else:
    print(f'{char} is not in {name}')


if char == 's': # == != < >>=
    print(f' s is equal to {char}')

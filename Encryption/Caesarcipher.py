
Key = 2

def read_plain_text(filename):
    with open(filename, "r") as file:
        plain_text = file.read()
    return plain_text


def caeser_char_cipher(char, key):
    if char.islower():
        pos = ord(char)-97
        new_pos = (pos+key)%26
        ciper_char = chr(new_pos+97)
        return ciper_char
    elif char.isupper():
        pos = ord(char) - 65
        new_pos = (pos + key) % 26
        ciper_char = chr(new_pos + 65)
        return ciper_char
    else:
        if ord(char) == 32:
            return char

def write_cipher_text(filename,char):
    with open(filename, "a") as file:
        file.write(char)


def main():
    plain_text = read_plain_text("PlainText")
    for char in plain_text:
        write_cipher_text("CipherText", caeser_char_cipher(char,Key))



main()
import  string


letters = "abbabcbdbabdbdbabababcbcbab"

def char_freq (letters):
    letter_dicti = {}
    for letter in letters:
        if letter.isalpha():
            if  not letter in letter_dicti.keys(): # add first time
                letter_dicti[letter] =1
            else:
                letter_dicti[letter] += 1
    print(letter_dicti)

char_freq(letters)

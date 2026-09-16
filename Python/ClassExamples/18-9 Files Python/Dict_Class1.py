
TEXT = "abbabcbdbabdbdbabababcbcbab"
dict_letters ={}


def char_freq(letters):
    global dict_letters
    for letter in letters:
        if letter in dict_letters:
            dict_letters[letter] += 1
        else:
            dict_letters[letter] = 1

    #for letter in letters:
    #    dict_letters[letter] +=1

    return dict_letters


print(char_freq(TEXT))
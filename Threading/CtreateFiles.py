import random
import string
import time


for number in range(10):
    sign_random = random.choice(string.punctuation)
    with open(f"file{number}", "a") as file:
        file.write(sign_random*100000)
        time.sleep(1)





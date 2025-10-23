import string
import requests

URL ="https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/days.txt"

def write_to_file (url):
    html_data = requests.get(url).text
    passwords = html_data.splitlines()
    for password in passwords:
        if password[0] in string.ascii_uppercase:
            with open("days.txt", "a") as file :
                file.write(password+"\n")

write_to_file(URL)

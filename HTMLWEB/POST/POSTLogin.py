import requests

URL = "https://hack-yourself-first.com/Account/Login"

# username , password
# name = ...

data ={ "Email": "shalomv@hotmail.com", "Password": "David1" }

html_data = requests.post(URL, data)

if "Hello"    not in html_data.text :
    print(" False")
else:
    print(data["Password"])
    print("You r great Cyber man / woman")


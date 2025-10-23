
import requests
from bs4 import BeautifulSoup


URL = "https://hack-yourself-first.com/Account/Login"
data= {"email": "shalom@hotmail.com","Password":"qazwsx" }

html_data = requests.post(URL,data)
print(html_data.text)
# getting the html STRING WEB SITE
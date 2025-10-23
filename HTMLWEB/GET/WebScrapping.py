
import requests
from bs4 import BeautifulSoup


URL = "https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/days.txt"
html_data = requests.get(URL).text
print(html_data)
# getting the html STRING WEB SITE

soup = BeautifulSoup( html_data , 'html.parser')
h1_tag = soup.find("h1").get_text()
h2_tag = soup.find_all("h2")
print(h2_tag)

for h2 in h2_tag:
    print(h2.get_text())

print(h1_tag)









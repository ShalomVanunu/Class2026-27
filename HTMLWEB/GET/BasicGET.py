
import requests


URL = "https://keithgalli.github.io/web-scraping/webpage.html"
html_data = requests.get(URL).text
print((html_data).split("h1")[1])


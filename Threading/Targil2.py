from bs4 import BeautifulSoup
import requests
import time
import threading

#sites = ["https://zoom.com","https://one.com","https://cnn.com"]

sites = ["https://www.ynet.co.il",

         "https://13tv.co.il",
         "https://edition.cnn.com",
         "https://www.youtube.com",
         "https://www.calcalist.co.il",
         "https://www.one.co.il",
         "https://www.google.co.il",
         "https://www.maariv.co.il"]


def read_site_and_save(site):
    site_content = requests.get(site).text
    soup = BeautifulSoup(site_content, 'html.parser')
    with open(site.split("//")[1],"w")as file:
        file.write(str(site_content.encode("utf-8")))
    print("Total_Time = ", time.perf_counter() - start)


start = time.perf_counter()
for site in sites:
    read_site_and_save(site)
    time.sleep(0.5)
print("Total_Time = ",time.perf_counter()-start)

start = time.perf_counter()

for site in sites:
    th = threading.Thread(target=read_site_and_save, args=(site,))
    th.start()




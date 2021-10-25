# pip install beautifulsoup4 lxml
import requests
from bs4 import BeautifulSoup

url = 'https://www.google.com/search?q=formula+1+results&'

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
#NAMES
full_page = requests.get(url, headers=headers)
soup = BeautifulSoup(full_page.content, "html.parser")
convert = soup.findAll("span", {"class": "tsp-w tsp-el tsp-db"})



for names in convert:  # get
    racers = names.text
    print(racers)

#Finish time


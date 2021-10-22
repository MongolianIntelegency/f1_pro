# pip install beautifulsoup4 lxml
import requests
from bs4 import BeautifulSoup


url = 'https://www.bbc.com/sport/formula1/latest'

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

req = requests.get(url, headers=headers)
src = req.text
print(src)

import sqlite3
import requests
from bs4 import BeautifulSoup as bs

# Open Database
conn = sqlite3.connect('scrape.db')
c = conn.cursor()

url = "https://www.wiggle.co.uk/cycle/clothing/"
page = requests.get(url)








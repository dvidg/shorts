import sqlite3
import requests
from bs4 import BeautifulSoup as bs

# Open Database
conn = sqlite3.connect('scrape.db')
c = conn.cursor()

# Open webpage
baseURL = "https://www.wiggle.co.uk/cycle/clothing/?g=" # base url ?g=1

# ?g=97 (48+1)
for i in range(1): #126 possible
	url = baseURL + str(i*48+1)
	page = requests.get(url)	
	soup = bs(page.text, 'html.parser')
	"""
	productDivs = soup.findAll("a", {"class": "bem-product-thumb__image-link--grid"})
	for div in productDivs:
		print div.find('a')['href']
	"""
	productLinks = [div.a for div in soup.findAll('div', attrs={'class' : "bem-product-thumb--grid"})]
	for link in productLinks:
		print(link['href'])


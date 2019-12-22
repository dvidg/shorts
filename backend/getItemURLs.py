"""
	Get items from each page of the URL

"""
import requests
import sqlite3
import ast
from bs4 import BeautifulSoup as bs

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

productList = []

#c.execute("""INSERT INTO categoryURLs (category, URLs) VALUES (?, ?)""", (cats[0],str(longUrls).strip('[]')))

def getURL(url):
	productURLs = []
	page = requests.get(url)	
	soup = bs(page.text, 'html.parser')
	productLinks = [a.findChildren("img")[0] for a in soup.findAll('a', attrs={'class' : "bem-product-thumb__image-link--grid"})]
	for x in productLinks:
		productURLs.append(x["src"])
	return productURLs # TODO: why is this in so many ]]]





c.execute("""SELECT category FROM categoryURLs;""")
cats=[i[0] for i in c.fetchall()]

# Remove [] around cats when moving away from single testing
for category in cats:
	c.execute("""SELECT URLs FROM categoryURLs WHERE category=?""", (category,))
	urls = ast.literal_eval([i[0] for i in c.fetchall()][0])
	
	if (category == "Baggy-Shorts"):
		productList.append([getURL(url) for url in urls])
		print(productList)

conn.commit()	

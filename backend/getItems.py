"""
	Get items from each page of the URL

"""
import requests
import sqlite3
from bs4 import BeautifulSoup as bs

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

c.execute("""DROP TABLE IF EXISTS categoryURLs""")

c.execute("""SELECT item,URL FROM mainCategories;""")
urls=c.fetchall()

c.execute("""CREATE TABLE categoryURLs (category, URLs)""")

itemNumber = [i*48+1 for i in range(50)]
pages = ["/?g="+str(i) for i in itemNumber] #/?g=1, /?g=49, /?g=97...
cats=[i[0] for i in urls]
urls=[i[1] for i in urls]
dictionary={}

for i in [urls[-1]]: #[urls[-1]] for testing
	# i is a https://www.wiggle.co.uk/cycle/Beanies
	page = requests.get(i)
	soup = bs(page.text, "html.parser")
	itemNumString = soup.find("div", {"class":"bem-paginator__text-block"}).text	
	numItems = int(itemNumString.strip().split()[-1]) # number of items

	# lastCat
	lastCats = [i for i in itemNumber if i > numItems]
	longUrls = [i+j for j in [pages[-len(lastCats)-1]]]
	
	c.execute("""INSERT INTO categoryURLs (category, URLs) VALUES (?, ?)""", (cats[0],str(longUrls)))
	cats.pop(0)

conn.commit()

	

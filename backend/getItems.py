"""
	Get items from each page of the URL

"""
import requests
import sqlite3
from bs4 import BeautifulSoup as bs

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

c.execute("""SELECT item,URL FROM mainCategories;""")
urls=c.fetchall()

pages = ["/?g="+str(i*48+1) for i in range(5)] #/?g=1, /?g=49, /?g=97...
cats=[i[0] for i in urls]
urls=[i[1] for i in urls]
dictionary={}

for i in [urls[-1]]: #[urls[-1]] for testing
	# i is a https://www.wiggle.co.uk/cycle/Beanies
	page = requests.get(i)
	soup = bs(page.text, "html.parser")
	itemNumString = soup.find("div", {"class":"bem-paginator__text-block"}).text	
	numItems = int(itemNumString.strip().split()[-1])# number of items
	print(numItems)
"""	
	longUrls = [i+j for j in pages]
	dictionary[cats[0]] = longUrls
	cats.pop(0)
"""

# <div class=""bem-noresults__alert-text"></div>

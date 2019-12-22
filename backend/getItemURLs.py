"""
	Get items from each page of the URL

"""
import requests
import sqlite3
import ast
from bs4 import BeautifulSoup as bs

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

#c.execute("""INSERT INTO categoryURLs (category, URLs) VALUES (?, ?)""", (cats[0],str(longUrls).strip('[]')))


c.execute("""SELECT category FROM categoryURLs;""")
cats=[i[0] for i in c.fetchall()]

# Remove [] around cats when moving away from single testing
for category in [cats[2]]:
	c.execute("""SELECT URLs FROM categoryURLs WHERE category=?""", (category,))
	urls = c.fetchall()[0][0]
	print(urls)


conn.commit()	

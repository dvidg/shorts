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

longUrls=[i+j for i in urls for j in pages]

print(longUrls)


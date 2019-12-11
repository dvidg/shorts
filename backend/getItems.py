"""
	Get items from each page of the URL
"""
import requests
import sqlite3
from bs4 import BeautifulSoup as bs

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

c.execute("""SELECT URL FROM mainCategories;""")
urls=c.fetchall()
urls=[i[0] for i in urls]
print(urls)

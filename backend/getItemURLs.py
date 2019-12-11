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


c.execute("""select * from categoryURLs;""")
urls=c.fetchone()
cats=urls[0]
urlList=ast.literal_eval(urls[1])

print(urlList[0])
print(cats)

conn.commit()	

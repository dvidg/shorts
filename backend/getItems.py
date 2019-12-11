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
urls=[i[1] for i in urls]
print(urls)
"""
?g=49
?g=97
?g=145
?g=193
"""
pages = ["/?g="+str(i*48+1) for i in range(100)] #/?g=1, /?g=49, /?g=97....

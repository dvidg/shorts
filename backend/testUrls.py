import requests
import sqlite3

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

c.execute("""SELECT item FROM mainCategories;""")
items=c.fetchall()
print(items)

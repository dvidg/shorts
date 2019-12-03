import requests
import sqlite3

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

c.execute("""SELECT item FROM mainCategories;""")
items=c.fetchall()
items=[i[0] for i in items]
items = [e.replace(" ", "-") for e in items]

print(items)

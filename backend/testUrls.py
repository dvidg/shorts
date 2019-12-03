import requests
import sqlite3

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

c.execute("""SELECT * FROM mainCategories;""")
items=c.fetchall()
categories=[i[0] for i in items]
items=[i[1] for i in items]
items = [e.replace(" ", "-") for e in items]
items = list(zip(categories, items))

failedList = []

c.execute("""ALTER TABLE mainCategories RENAME TO tempMainCategories;""")
c.execute("""CREATE TABLE mainCategories (body, item, URL)""")

def testURL(itemList):
	url = "https://www.wiggle.co.uk/cycle/"+itemList[1]
	r=requests.get(url)
	if r.status_code != 200:
		failedList.append(category,r.status_code)
	else:
		c.execute("""INSERT INTO mainCategories (body, item, URL) VALUES (?, ?, ?)""", (itemList[0], itemList[1], url))

[testURL(i) for i in items]

if(len(failedList)==0):
	print("no failures")
else:
	print(failedList)

conn.commit()

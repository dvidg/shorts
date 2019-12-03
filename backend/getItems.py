import requests
import sqlite3

conn = sqlite3.connect('scrape.db')
c = conn.cursor()

c.execute("""SELECT item FROM mainCategories;""")
items=c.fetchall()
items=[i[0] for i in items]
items = [e.replace(" ", "-") for e in items]

failedList = []

def testURL(category):
	url = "https://www.wiggle.co.uk/cycle/"+category
	r=requests.get(url)
	if r.status_code != 200:
		failedList.append(category,r.status_code)

[testURL(i) for i in items]

if(len(failedList)==0):
	print("no failures")
else:
	print(failedList)

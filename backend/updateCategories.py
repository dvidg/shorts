import sqlite3
import requests
from bs4 import BeautifulSoup as bs

# Open Database
conn = sqlite3.connect('scrape.db')
c = conn.cursor()
c.execute("""DROP TABLE IF EXISTS mainCategories""")

# Open webpage
baseURL = "https://www.wiggle.co.uk/cycle/clothing/?g=" # base url ?g=1


f = open("allCategories.txt","w+")


# Open each page of items
allCategories = []
shortCategories=[]

for i in range(1): #126 possible
	print(i)
	url = baseURL + str(i*48+1)
	page = requests.get(url)	
	soup = bs(page.text, 'html.parser')

	# Get each item on page
	productLinks = [div.a for div in soup.findAll('div', attrs={'class' : "bem-product-thumb--grid"})]

	# Open each item
	for link in productLinks:
		productPage = requests.get(link['href'])
		newSoup = bs(productPage.text, 'html.parser')

		# Get ['Home', 'Clothing', 'Socks and Underwear', 'Socks']
		productType = str([li.a['title'] for li in newSoup.findAll('li', attrs={'class' : "bem-breadcrumb__list-item"})])
		print(productType[0])
		print(productType)
		print(productType[-2:])
		shortCategories.append(productType[-2:])
		allCategories.append(productType)

print(shortCategories)
shortCategories = list(dict.fromkeys(shortCategories))
#allCategories = list(dict.fromkeys(allCategories))

print(shortCategories)

c.execute("""CREATE TABLE mainCategories (body, item)""")

for x in shortCategories:
	f.write(x[0] + x[1] +"\n")
	c.execute("""INSERT INTO mainCategories (body, item) VALUES (?, ?)""", (x[0],x[1]))

f.close()
conn.commit()


print("done")
	

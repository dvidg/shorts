import sqlite3
import requests
import ast
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
		productType = [li.a['title'] for li in newSoup.findAll('li', attrs={'class' : "bem-breadcrumb__list-item"})]
		shortCategories.append(productType[-2:])
		#allCategories.append(productType)

shortCategories =[list(x) for x in set(tuple(x) for x in shortCategories)]
#allCategories = list(dict.fromkeys(allCategories))

c.execute("""CREATE TABLE mainCategories (body, item)""")

for x in shortCategories:
	try:
		f.write(x[0] + x[1] +"\n")
		c.execute("""INSERT INTO mainCategories (body, item) VALUES (?, ?)""", (x[0],x[1]))
	except:
		pass

f.close()
conn.commit()


print("done")
	

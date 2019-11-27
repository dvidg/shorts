import sqlite3
import requests
from bs4 import BeautifulSoup as bs

# Open Database
conn = sqlite3.connect('scrape.db')
c = conn.cursor()

# Open webpage
baseURL = "https://www.wiggle.co.uk/cycle/clothing/?g=" # base url ?g=1


f = open("allCategories.txt","w+")


# Open each page of items
allCategories = []

for i in range(50): #126 possible
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
		
		allCategories.append(productType)

allCategories = list(dict.fromkeys(allCategories))

c.execute("""CREATE TABLE mainCategories
                 (categories)""")



for x in allCategories:
	f.write(x+"\n")
	c.execute("insert into mainCategories (categories) values (?)",
            (x,))

f.close()



print("done")
	
	

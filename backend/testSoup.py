"""
	Basic template for soup and url usage

"""
import sqlite3
import requests
from bs4 import BeautifulSoup as bs

# Open Database
conn = sqlite3.connect('scrape.db')
c = conn.cursor()

# Open webpage
baseURL = "https://www.wiggle.co.uk/cycle/clothing/?g=" # base url ?g=1


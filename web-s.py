from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# executable path to the chrome browser
driver = webdriver.Chrome("/mnt/c/chromedriver/chromedriver.exe")

products = []	# list of products scraped
prices = []		# list to store price of the product
ratings = []	# list to store rating of the product

driver.get("https://www.flipkart.com/search?q=laptop")
# extract div tags with the relevant class names

content = driver.page_source
soup = BeautifulSoup (content, "lxml")
count = 1
for a in soup.findAll ('a', href = True, attrs = {'class':'_31qSDS'}) and count < 50:
	name = a.find ('div', attrs = {'class':'_3sU53n'})
	price = a.find ('div', attrs = {'class':'_1vC40E _2rQ-NK'})
	rating = a.find ('div', attrs = {'class':'hGSR34 _2beYZw'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)
	count = count + 1
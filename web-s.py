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
for a in soup.findAll ('a', href = True, attrs = {'class':'_31qSD5'}) and count < 50:
	name = a.find ('div', attrs = {'class':'_3wU53n'})
	price = a.find ('div', attrs = {'class':'_1vC4OE _2rQ-NK'})
	rating = a.find ('div', attrs = {'class':'hGSR34'})
	products.append(name.text)
	prices.append(price.text)
	ratings.append(rating.text)
	count = count + 1

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')
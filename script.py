print('Webscraper file is')
#use Beautiful Soup to Web Scraper
#https://oxylabs.io/blog/python-web-scraping

import requests
url='https://www.numbeo.com/cost-of-living/country_result.jsp?country=Japan'
response = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title) #just for clarification of title accessed

#print values found in USA document
price_list = []

element = soup.select('span.first_currency')
for title in element:
    price_list.append(title.text)

print(price_list)

#use Beautiful Soup to Web Scraper
#https://oxylabs.io/blog/python-web-scraping

import requests
url='https://www.numbeo.com/cost-of-living/country_result.jsp?country=Japan'
response = requests.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')
print('\n', soup.title) #just for clarification of title accessed

url2 = 'https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States'
response2 = requests.get(url2)
soup2 = BeautifulSoup(response2.text, 'html.parser')
print(soup2.title) #just for clarification of title accessed

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Computed Constants:
jyp2usd_figure = 0 #Yen to USD Conversion Rate
avgMoNetSalary_JP = 0
avg_mo_single_expense_JP = 0
usd_Mo_Net_Salary_JP = 0 #Mo Salary converted into USD
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#print values found in USA document
price_list = []
avg_mo_expense = []

element = soup.select('span.first_currency')
for title in element:
    price_list.append(title.text)

#Average Mo. Net Salary in Japan (After Tax)
avgMoNetSalary1 = (price_list[-2])
avgMoNetSalary_JP = float(avgMoNetSalary1.replace('¥', '').replace(',', ''))

#1 Bd Apartment in City Center
inside_city_apt_1person0 = (price_list[-8])
inside_city_apt_1person = float(inside_city_apt_1person0.replace('¥', '').replace(',', ''))

#1 Bd Apartment outside City Center
outside_city_apt_1person0 = (price_list[-7])
outside_city_apt_1person = float(outside_city_apt_1person0.replace('¥', '').replace(',', ''))

#Average Mo. Expense for a single person in Japan (NI Rent)
aysms = soup.select('span.in_other_currency')
for title in aysms:
    avg_mo_expense.append(title.text)
avg_mo_single_expense = avg_mo_expense[1]
avg_mo_single_expense_JP = float(avg_mo_single_expense.replace('(', '').replace(')', '').replace('¥', '').replace(',', ''))

#access foreign conversion
jpy_usa="https://www.getexchangerates.com/jpy/"
response = requests.get(jpy_usa)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title,'\n')

td_options = []
figure = soup.select('td')
for title in figure:
    td_options.append(title.text)

jyp2usd_figure = float(td_options[2])

#Convert to USD ^^^^^^^^^^^^^^^^^^^^^^^^^^^(IMPORTANT FIGURES)
usd_Mo_Net_Salary_JP = (jyp2usd_figure) * (avgMoNetSalary_JP)
usd_single_exp_JP = (jyp2usd_figure) * (avg_mo_single_expense_JP)
usd_1bdInCity_JP = (jyp2usd_figure) * (inside_city_apt_1person)
usd_2bdInCity_JP = (jyp2usd_figure) * (outside_city_apt_1person)

print(usd_Mo_Net_Salary_JP)
print(usd_single_exp_JP)
print(usd_1bdInCity_JP)
print(usd_2bdInCity_JP)
print('______________\n')

##########################################################################
price_list_US = []
avg_mo_expense_US = []

#Average Mo. Net Salary in USA (After Tax)
element2 = soup2.select('span.first_currency')
for title in element2:
    price_list_US.append(title.text)

avgMoNetSalary1_US = (price_list_US[-2])
avgMoNetSalary_US = float(avgMoNetSalary1_US.replace('$', '').replace(',', ''))
print(avgMoNetSalary_US)

#1 Bd Apartment in City Center
inside_city_apt_1person0_US = (price_list_US[-8])
inside_city_apt_1person_US = float(inside_city_apt_1person0_US.replace('$', '').replace(',', ''))
print(inside_city_apt_1person_US)

#1 Bd Apartment outside City Center
outside_city_apt_1person0_US = (price_list_US[-7])
outside_city_apt_1person_US = float(outside_city_apt_1person0_US.replace('$', '').replace(',', ''))
print(outside_city_apt_1person_US)

#Average Mo. Expense for a single person in USA (NI rent)



#MatPlotLib
#display disposable income
#display percentage of 







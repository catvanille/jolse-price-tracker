import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import smtplib
import pandas as pd
URL = 'https://jolse.com/category/best/25/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    for element in soup.findAll('div', attrs={'class': 'description'}):
        product = element.find('strong', attrs={'class': 'name'}).text.strip()[15:]
        #price = element.find('ul', class_='xans-element-').find('li', class_='xans-record-').find('span').text.strip()
        price = element.find('ul', attrs={'class': 'xans-element- xans-product xans-product-listitem spec'}).text.strip()[10:]
        old_price, new_price = price.split('USD ')
        products.append(product)
        oldprices.append(float(old_price))
        newprices.append(float(new_price))
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

def check_duplicates(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not(x in seen or seen_add(x))]

products = []
oldprices = []
newprices = []

# yoink price
check_price()

# remove duplicates
n_products = check_duplicates(products)
n_oldprices = check_duplicates(oldprices)
n_newprices = check_duplicates(newprices)

# add data to products.csv
df = pd.DataFrame({'Product': products, 'Old Price': oldprices, 'New Price': newprices})
df.to_csv('products.csv', index=False, encoding='utf-8')


"""
using chromedriver
"""
# driver = webdriver.Chrome()
# driver.get('https://jolse.com/category/best/25/')

# content = driver.page_source
# soup = BeautifulSoup(content, features="html.parser")

# for element in soup.findAll('div', attrs={'class': 'description'}):
#     product = element.find('strong', attrs={'class': 'name'}).text.strip()[15:]
#     #price = element.find('ul', class_='xans-element-').find('li', class_='xans-record-').find('span').text.strip()
#     price = element.find('ul', attrs={'class': 'xans-element- xans-product xans-product-listitem spec'}).text.strip()[10:]
#     old_price, new_price = price.split('USD ')
#     products.append(product)
#     oldprices.append(float(old_price))
#     newprices.append(float(new_price))
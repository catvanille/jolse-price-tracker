import requests
from bs4 import BeautifulSoup
# from selenium import webdriver
import smtplib
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    for element in soup.findAll('div', attrs={'class': 'description'}):
        link = element.find('a')['href']
        if 'display/2' in link:
            continue
        else:
            links.append(URL+link)
        product = element.find('strong', attrs={'class': 'name'}).text.strip()[len('Product Name: '):]
        thumbnail = element.find('img')['src'] # to fix, currently prints //img.echosting.cafe24.com/design/skin/admin/en_US/btn_prd_zoom.gif
        get_price = element.find('ul', attrs={'class': 'xans-element- xans-product xans-product-listitem spec'}).text.strip()[len('Price USD '):]
        if '\n\n' in get_price: # means theres a disc
            get_price = get_price.split(' \n\n USD ')
            og_price = get_price[0]
            space_split = get_price[1].find(' ')
            curr_price = get_price[1][:space_split]
            percent_split = get_price[1].find('%')
            percent = get_price[1][space_split+2:percent_split]
        else:
            curr_price = get_price
        products.append(product)
        ogprices.append(float(og_price))
        currprices.append(float(curr_price))
        percentoff.append(percent)
        if element.find('img', attrs={'alt': 'Out-of-stock'})==None:
            stock.append(1) # in stock
        else:
            stock.append(0)
        
def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

products = []
ogprices = []
currprices = []
percentoff = []
links = []
stock = []
for i in range(1, 86):
    URL = 'https://jolse.com/category/lipcare/4745/' + '?page=' + str(i)
    check_price()

#add data to products.csv
df = pd.DataFrame({'Product': products, 'Og Price': ogprices, 'Curr Price': currprices, 'Discount': percentoff, 'Link': links, 'Stock': stock})
# sort by largest to smaller discount
df = df.sort_values(by=['Discount'], ascending=False)
df.to_csv('yoinkproducts.csv', index=False, encoding='utf-8')

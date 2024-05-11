from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

# Initialize lists
links = []
products = []
oldprices = []
newprices = []
percentoff = []
stock = []

'''
scrapper
'''
def check_price(URL):

   page = requests.get(URL, headers=headers)
   soup = BeautifulSoup(page.content, 'html.parser')

   for element in soup.findAll('div', attrs={'class': 'description'}):
      link = element.find('a')['href']
      if 'display/2' in link:
         continue
      else:
         # make sure to add prepend for link
         link = f'https://jolse.com{link}'
         links.append(link)
      product = element.find('strong', attrs={'class': 'name'}).text.strip()[15:]
      price = element.find('ul', attrs={'class': 'xans-element- xans-product xans-product-listitem spec'}).text.strip()[10:]
      if 'USD ' in price:
         old_price, new_price = price.split('USD ')
      else:
         old_price = price
         new_price = price
      products.append(product)
      oldprices.append(float(old_price))
      newprices.append(float(new_price))
      percentoff.append(int(float(old_price) - float(new_price)) / float(old_price) * 100)
      if 'src="/web/upload/icon_201906191605023500.jpg' in element.find('div', attrs={'class': 'icon'}).text.strip() == True:
         stock.append(0)
      else:
         stock.append(1)
   
   # Return the scraped data as a dictionary
   return {
      "products": products,
      "oldprices": oldprices,
      "newprices": newprices,
      "links": links,
      "stock": stock
   } 

'''
grab skincare category
'''
def yoink_skincare():
   skincare_data = {
      "products": [],
      "oldprices": [],
      "newprices": [],
      "links": [],
      "stock": []
   }

   # range = total pages(currently 85)
   for i in range(1, 2):
      URL = 'https://jolse.com/category/skincare/1018/' + '?page=' + str(i)
      data = check_price(URL)
      skincare_data["products"].extend(data["products"])
      skincare_data["oldprices"].extend(data["oldprices"])
      skincare_data["newprices"].extend(data["newprices"])
      skincare_data["links"].extend(data["links"])
      skincare_data["stock"].extend(data["stock"])

   return skincare_data

# Route to return scraped data as JSON
@app.route('/data')
def get_data():
   data = yoink_skincare()
   return jsonify(data)

if __name__ == '__main__':
   app.run(debug=True)
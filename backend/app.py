from flask import Flask, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
#from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from supabase_client import supabase
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

headers = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


'''
scrapper
'''
def check_price(URL):

   page = requests.get(URL, headers=headers)
   soup = BeautifulSoup(page.content, 'html.parser')

   data = []

   for element in soup.findAll('div', attrs={'class': 'description'}):
      link = element.find('a')['href']
      if 'display/2' in link:
         continue
      else:
         # make sure to add prepend for link
         link = f'https://jolse.com{link}'
         
      product = element.find('strong', attrs={'class': 'name'}).text.strip()[15:]
      price = element.find('ul', attrs={'class': 'xans-element- xans-product xans-product-listitem spec'}).text.strip()[10:]
      if 'USD ' in price:
         old_price, new_price = price.split('USD ')
      else:
         old_price = price
         new_price = price

      old_price = float(old_price)
      new_price = float(new_price)
      percent_off = (old_price - new_price) / old_price * 100
      in_stock = 0 if 'src="/web/upload/icon_201906191605023500.jpg' in element.find('div', attrs={'class': 'icon'}).text.strip() else 1

      data.append({
         "product": product,
         "old_price": old_price,
         "new_price": new_price,
         "link": link,
         "stock": in_stock,
         "percent_off": percent_off
      })
      
   
   # Return the scraped data
   return data

'''
grab skincare category
'''
def yoink_skincare():
   skincare_data = []

   # range = total pages(currently 85)
   # NOTE: seems to bug out when increasing range
   for i in range(1, 2):
      URL = 'https://jolse.com/category/skincare/1018/' + '?page=' + str(i)
      skincare_data.extend(check_price(URL))

   # inset data into supabase
   supabase.table('skincare_products').upsert(skincare_data).execute()

# Route to return scraped data as JSON
@app.route('/data')
def get_skincare_data():
   response = supabase.table('skincare_products').select('*').execute()
   data = response.data
   return jsonify(data)

if __name__ == '__main__':
   # schedule yoinking once every day
   ## scheduler = BackgroundScheduler()
   ## scheduler.add_job(yoink_skincare, 'interval', days=1, start_date=datetime.now())
   ## scheduler.start()
   yoink_skincare()

   app.run(debug=True)
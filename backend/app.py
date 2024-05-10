from flask import Flask, jsonify
import scraper

app = Flask(__name__)

products = []
oldprices = []
newprices = []
percentoff = []
links = []
stock = []

# for scraping
@app.route('/scrape')
def scrape():
   scraper.check_price()
   return 'scraping complete'

# Route to return scraped data as JSON
@app.route('/data')
def get_data():
   data = {
      "products": products,
      "oldprices": oldprices,
      "newprices": newprices,
      # "discount": percentoff,
      "links": links,
      "stock": stock
   }
   return jsonify(data)

if __name__ == '__main__':
   app.run(debug=True)
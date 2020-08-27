from flask import Flask,jsonify,render_template,send_from_directory
import os
import pymongo
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('img', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('vendor', path)

@app.route('/',methods=['GET'])
def index():
   data=get_data_from_db()
   return render_template('index.html',data=data)

def get_data_from_db():
   dbClient=pymongo.MongoClient(os.getenv('MONGO_TOKEN'))
   recordsCollection=dbClient['Ads'].records
   data={}
   data['total_ads']=recordsCollection.count_documents({'profit_average':{'$gt':999}})
   data['total_confidentials']=recordsCollection.count_documents({'property_name':'CONFIDENTIAL'})
   data['items']=[]
   for item in recordsCollection.find({'profit_average':{'$gt':999}}):
      dd={
         'id':item['id'],
         'name':item['title'],
         'price':item['price'],
         'bids':item['bid_count'],
         'category':item['category'],
         'monthly_profit':item['profit_average'],
         'country':item['country_name'],
         'inserted_data':item['inserted_timestamp'],
         
      }
      
      try:dd['time_end']=item['time_end']
      except KeyError:dd['time_end']=''

      try:dd['buynow_price']=item['buy_it_now']
      except KeyError:dd['buynow_price']=''
      
      data['items'].append(dd)

   
   return data

if __name__ == '__main__':
   app.run(debug=True)


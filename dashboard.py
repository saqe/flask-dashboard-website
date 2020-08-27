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
   
   
   countries={}
   for i in recordsCollection.aggregate([{'$group' : { '_id' : '$country_name', 'count' : {'$sum' : 1}}},{ '$sort': { 'count': -1 }},{ '$limit' : 5 }]):
      countries[i['_id']]=i['count']
   data['countries_name']=list(countries.keys())
   data['countries_value']=list(countries.values())
   

   data['items']=[]

   for item in recordsCollection.find(
      {'profit_average':{'$gt':999}},
      {
         'id': 1,
         'title': 1,
         'price': 1,
         'category': 1,
         'sale_method':1,
         'profit_average': 1,
         'monetization': 1,
         'inserted_timestamp': 1,
         'buy_it_now': 1,
         'inserted_timestamp': 1,
         'time_end': 1,
         'country_name': 1,
         }
      ):
      data['items'].append(item)
   return data

if __name__ == '__main__':
   app.run(debug=True)


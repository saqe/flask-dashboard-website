import pymongo
from datetime import datetime

def getDashboardData(MONGO_TOKEN):
   dbClient=pymongo.MongoClient(MONGO_TOKEN)
   recordsCollection=dbClient['Ads'].records
   data={}
   data['total_ads']=recordsCollection.count_documents({'profit_average':{'$gt':999}})
   data['total_confidentials']=recordsCollection.count_documents({'property_name':'CONFIDENTIAL'})
   data['total_confidentials_per']=int((data['total_confidentials']/data['total_ads'])*100)
   date=datetime.now()
   data['updated_today']=recordsCollection.count_documents({"last_updated": {"$gte": datetime(date.year,date.month,date.day)}})
   data['added_today']=recordsCollection.count_documents({"inserted_timestamp": {"$gte": datetime(date.year,date.month,date.day)}})
   
   d={}
   for x in recordsCollection.aggregate([{'$group' : { '_id' : '$sale_method', 'count' : {'$sum' : 1}}},{ '$sort': { 'count': -1 }},{ '$limit' : 3 }]):
      d[x['_id']]=x['count']   
   data['salesMethod_name']=list(d.keys())
   data['salesMethod_value']=list(d.values())

   d={}
   for x in recordsCollection.aggregate([{'$group' : { '_id' : '$category', 'count' : {'$sum' : 1}}},{ '$sort': { 'count': -1 }},{ '$limit' : 10 }]):
      d[x['_id']]=x['count']
   data['categories_name']=list(d.keys())
   data['categories_value']=list(d.values())

   d={}
   for x in recordsCollection.aggregate([{'$group' : { '_id' : '$country_name', 'count' : {'$sum' : 1}}},{ '$sort': { 'count': -1 }},{ '$limit' : 5 }]):
      d[x['_id']]=x['count']
   data['countries_name']=list(d.keys())
   data['countries_value']=list(d.values())
   
   d={}
   for x in recordsCollection.aggregate([{'$group' : { '_id' : '$monetization', 'count' : {'$sum' : 1}}},{ '$sort': { 'count': -1 }},{ '$limit' : 10 }]):
      if x['_id'] is None:x['_id']='N/A'
      d[x['_id']]=x['count']   
   data['monetization_name']=list(d.keys())
   data['monetization_value']=list(d.values())

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
         'time_end': 1,
         'country_name': 1,
         }
      ):
      try:item['time_end']=item['time_end'][:10]
      except KeyError:pass

      data['items'].append(item)
   return data
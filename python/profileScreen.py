import pymongo
from datetime import datetime

def profileDashboard(MONGO_TOKEN,profile_id):
    dbClient=pymongo.MongoClient(MONGO_TOKEN)
    return dbClient['Ads'].records.find_one({'id':profile_id})
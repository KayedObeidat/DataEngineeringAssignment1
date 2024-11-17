import requests
import pymongo
import datetime

API = 'https://api.api-ninjas.com/v1/randomuser'
KEY = 'hXPx5QiEbY/DeCj7uQNRag==Tt38qOUsnT9LdHOy'

client = pymongo.MongoClient("mongodb://localhost:27017")
DB = client['UsersAPI']
CollectionName = DB['Users']

timestamp = datetime.datetime.now()

for i in range(10000):  
    response = requests.get(API, headers={'X-Api-Key': KEY})

    data = response.json()

    if isinstance(data, dict):
        data['createdAt'] = timestamp
        CollectionName.insert_one(data)
    elif isinstance(data, list):  
        for user in data:
            user['createdAt'] = timestamp
        CollectionName.insert_many(data)

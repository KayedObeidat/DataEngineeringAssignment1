# DataEngineeringAssignment1

# Overview
In this code, I have used the ninja API to extract data of random users, The data contain below fields:
- Username: String
- Sex: String
- Address: String
- Email: String
- Birthday: String
- CreatedAt: Timestamp


# Code
To satisfy the assignment requirement, I used the following libraries:
- requests: To send requests to the target API
- pymongo: To connect to MongoDB
- datetime: To generate the time and date

## Connect to the Database
client = pymongo.MongoClient("mongodb://localhost:27017")

## Initiating the DB and Collection:
DB = client['UsersAPI']
CollectionName = DB['Users']

## Code logic
A loop that runs 10000 times was added to since the API returns only one document per hit,
After that, in each request, I'm sending the API key using the below line and paring the results to JSON format:
response = requests.get(API, headers={'X-Api-Key': KEY})
data = response.json()

If the returned data was returned as a dictionary, I used the below logic:
f isinstance(data, dict):
        data['createdAt'] = timestamp
        CollectionName.insert_one(data)

If the returned data was returned as a list, I used the below logic:
elif isinstance(data, list):  
        for user in data:
            user['createdAt'] = timestamp
        CollectionName.insert_many(data)

# DB Result Instance:
{
  "_id": {
    "$oid": "673a425754309ea017b87130"
  },
  "username": "nicholas47",
  "sex": "F",
  "address": "4195 Trujillo Summit Suite 597, Port Benjamin, WA 13656",
  "name": "Cristina Richmond",
  "email": "amurphy@hotmail.com",
  "birthday": "1933-11-08",
  "createdAt": {
    "$date": "2024-11-17T22:21:48.205Z"
  }
}

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

## Preprocessing Functions
- process_text: Converts text to lowercase and tokenizes it using regular expressions.
- remove_stopwords_and_punctuation: Removes stopwords (common words like "and", "the", etc.) and short words (length <= 1).
- emmatize_words: Lemmatizes the words in the text using spaCy, reducing them to their base form (e.g., "running" becomes "run").

## Word Frequency Analysis
- get_most_frequent_words: Calculates the frequency of words from the documents
-  The bar chart shows the 10 most frequent words and their count. Since the data we have contains names, addresses, and email addresses the word "com" was the most frequent word used, and then yahoo. hotmail, gmail, apt, suite, port, box, lake, and west in order
![image](https://github.com/user-attachments/assets/fdc46761-85e8-4714-bb65-e0e0c2d581d7)
- The word count figure shows the most common word in a bigger text, it shows all the items that were presented by the bar chart
  ![image](https://github.com/user-attachments/assets/a96e969c-1d65-4196-87b7-4411fbf29499)


## Spelling Mistakes Detection
- find_spelling_mistakes: Uses the SpellChecker library to identify misspelled words in the dataset.

## Sample data after processing
{
  "_id": {
    "$oid": "673a3935826aafa2092b314c"
  },
  "username": "mhayden",
  "sex": "F",
  "address": "829 Hodges Plains Apt. 575, Brooksbury, MD 19524",
  "name": "Angela Hall",
  "email": "lisarowe@gmail.com",
  "birthday": "1949-07-18",
  "createdAt": {
    "$date": "2024-11-17T21:43:00.062Z"
  },
  "processed_text": "829 hodge plain apt 575 brooksbury md 19524 angela hall lisarowe gmail com"
}

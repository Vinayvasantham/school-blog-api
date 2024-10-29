from pymongo import MongoClient

# Connect to the local MongoDB instance
client = MongoClient('localhost', 27017)  # default MongoDB port

# Access a database
db = client.test_database  # replace with your database name

# Access a collection
collection = db.test_collection  # replace with your collection name

print("Connection Successful!")

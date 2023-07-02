from pymongo import MongoClient

#MongoDB connection string
url = "mongodb+srv://admin:admin@cluster0.v4jjizu.mongodb.net/pytech"

#call MongoClient
client = MongoClient(url)

#connect to pytech db
db = client.pytech

#print collections
print(db.list_collection_names)

#end message
input("\n End of program, press any key to exit...")

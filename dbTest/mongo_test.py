import pymongo

client = pymongo.MongoClient('localhost', 27017)

client.close()
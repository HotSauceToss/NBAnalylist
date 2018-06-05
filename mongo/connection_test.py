import pymongo
from urllib.parse import quote


mongourl = "mongodb+srv://admin:" + quote("H@ns945369") + "@cluster0-l6smj.mongodb.net/test?retryWrites=true"
client = pymongo.MongoClient(mongourl)
db = client.test

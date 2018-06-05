import pymongo
from urllib.parse import quote


mongourl = "mongodb+srv://admin:" + quote("H@ns945369") + "@cluster0-l6smj.mongodb.net/test?retryWrites=true"
conn = pymongo.MongoClient(mongourl)
db = conn.test
players = db.players
players.delete_many({})
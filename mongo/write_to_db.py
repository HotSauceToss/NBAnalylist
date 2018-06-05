import pymongo
from urllib.parse import quote


mongourl = "mongodb+srv://admin:" + quote("H@ns945369") + "@cluster0-l6smj.mongodb.net/test?retryWrites=true"
conn = pymongo.MongoClient(mongourl)
db = conn.test
players = db.players
db.players.create_index([('Players', pymongo.ASCENDING)], unique=True)
## Writes to the MongoDB instance
# @param data list of dictionary entries to be inserted as documents
#       Must be more than one
def writeToMongo(data):

    # Invalid according to params
    if(len(data) < 1): raise IndexError
    # Insert one doc
    elif(len(data) == 1): players.insert_one(data[0])
    # Insert list of docs
    else: 
        players.insert_many(data)
    for p in players.find({'Player' : 'James Harden'}):
        print(p)


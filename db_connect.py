import pymongo

client = pymongo.MongoClient("mongodb+srv://admin:BrDtRoW7ZNDT3Wyn@headlines-db.a3a1p.mongodb.net/tvp-vs-tvn?retryWrites=true&w=majority")
db = client.tvp_vs_tvn
tvp = db.tvp
tvn = db.tvn

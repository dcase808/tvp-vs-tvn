import pymongo

client = pymongo.MongoClient("xxx")
db = client.tvp_vs_tvn
tvp = db.tvp
tvn = db.tvn
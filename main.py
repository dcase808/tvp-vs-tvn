import pymongo
import datetime


client = pymongo.MongoClient("mongodb+srv://admin:BrDtRoW7ZNDT3Wyn@fastapi-demo.lpfv5.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
tvp = db.tvp
tvn = db.tvn

entry_tvp = {
    "headline": "Donald Tusk chce śmierci Polaków!!",
    "date": datetime.datetime.utcnow()
}
entry_tvp2 = {
    "headline": "Schetyna też!!",
    "date": datetime.datetime.utcnow()
}
entry_tvn = {
    "headline": "Kaczyński kradnie!!",
    "date": datetime.datetime.utcnow()
}
entry_tvn2 = {
    "headline": "A ziobro to zero",
    "date": datetime.datetime.utcnow()
}

entries_tvp = [entry_tvp, entry_tvp2]
entries_tvn = [entry_tvn, entry_tvn2]


db.tvp.insert_many(entries_tvp)
db.tvn.insert_many(entries_tvn)
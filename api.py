from fastapi import FastAPI
from models import PyObjectId, headlines
from db_connect import tvp, tvn
from typing import Optional

app = FastAPI()

@app.get('/get-by-date/{site}/{year}/{month}/{day}')
async def get_by_year(year: int, month: int, day: int, site: str):
    if site == 'tvp':
        data = []
        for i in tvp.find():
            if i['date'].year == year and i['date'].month == month and i['date'].day == day:
                data.append(headlines(**i))
        return {'tvp': data}
    elif site == 'tvn':
        data = []
        for i in tvn.find():
            if i['date'].year == year and i['date'].month == month and i['date'].day == day:
                data.append(headlines(**i))
        return {'tvn': data}
    else:
        return {'error': 'specify site'}
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .db.Db import Db
from pydantic import BaseModel
import json
import datetime


class SessionInfo(BaseModel):
    time: datetime.datetime
    title: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get requests


@app.get("/get_last_title")
async def last_title():
    return Db.get_last_title()


@app.get("/get_total_time")
async def total_time():
    return Db.get_total_time()


# Post requests


@app.post("/insert_session_info")
async def insert_session_info(req: Request, data: SessionInfo):
    reqData = await req.json()
    print(reqData["time"])
    print(reqData["title"])
    spentTime = reqData["time"]
    # x = time.strptime(spentTime, "%H:%M:%S")
    Db.insert_time_calculation_session_info(reqData['time'], reqData["title"])
    print(Db.calculate_time_difference())
    print(reqData)
    return {json.dumps(reqData)}

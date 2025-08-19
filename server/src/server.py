from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .db.Db import Db
from pydantic import BaseModel
import datetime
from .utils.ISO_parse import ISO_parse
from .utils.reverse_title import reverse_and_split_title


class SessionInfo(BaseModel):
    spentTime: str
    startTime: datetime.datetime
    endTime: datetime.datetime
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
    # spentTime = datetime.datetime.fromisoformat(reqData["time"])
    # print()
    print(data)
    Db.insert_session_info(
        data.spentTime, 
        str(data.endTime), 
        str(data.startTime), 
        reverse_and_split_title(data.title)
    )
    print(Db.get_all_session_info())
    # Db.insert_session_info("2hour", "title")
    return {"Hell": "Hell"}

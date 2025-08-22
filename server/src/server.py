from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from .db.Db import Db
from pydantic import BaseModel
import datetime
from .utils.ISO_parse import ISO_parse
from .utils.reverse_title import reverse_and_split_title
from .models.SessionModel import SessionModel
from collections import defaultdict
from pprint import pprint

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

time_tree = defaultdict(lambda: defaultdict(list))


@app.post("/insert_session_info")
async def insert_session_info(req: Request, data: SessionModel):

    # Splitting titles based on " - " delimiter
    title_parts = [s.strip() for s in reverse_and_split_title(data.title).split("-")]
    while len(title_parts) < 3: 
        title_parts.append("")

    mainTitle = title_parts[0] 
    subtitle1 = title_parts[1]
    subtitle2 = title_parts[2]

    Db.insert_session_info(
        data.spentTime,
        str(data.endTime),  
        str(data.startTime),
        mainTitle,
        subtitle1,
        subtitle2,
    )
    all_session = Db.get_all_session_info()
    last_session = Db.get_session_info_by_id([len(all_session)])
    global time_tree  # Access the global time_tree

    print(f"database -> {all_session}", sep="\n")

    
    for i in last_session: 
        print("Itme ->", i) 
        id, spentTime, endTime, startTime, mainTitle, subtitle1, subtitle2 = i
 
        time_tree[mainTitle][subtitle1].append(
            {
                "subtitle2": subtitle2,
                "spentTime": spentTime,  # Or however you are getting the time
                "startTime": startTime,
                "endTime": endTime,
            }  
        )
    print("Time Tree -> ")
    pprint(time_tree) 

    return {"last session": last_session}

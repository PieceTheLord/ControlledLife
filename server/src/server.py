from collections import defaultdict
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from .utils.time_tree_converter import time_tree_converter
from .db.Db import Db
from .utils.reverse_title import reverse_and_split_title
from .models.SessionModel import SessionModel
from .models.SessionData import SessionData

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Get requests


@app.get("/get_last_session")
async def get_last_session():
    last_session = Db.get_last_session()

    if not last_session:
        return {
            "mainTitle": "No last session found",
            "subtitle1": {
                "title": "",
                "subtitle2": {
                    "title": "",
                    "endTime": "",
                    "startTime": "",
                },
            },
        }

    for session in last_session:
        mainTitle, subtitle1, subtitle2, endTime, startTime, spentTime  = session
    print(spentTime, endTime, startTime, mainTitle, subtitle1, subtitle2)

    last_session_time_tree = SessionData(
        mainTitle, subtitle1, subtitle2, endTime, startTime, spentTime
    ).to_dict()

    print("Last session time tree :", last_session_time_tree)

    return last_session_time_tree


@app.get("/get_all_sessions")
async def get_all_sessions():
    all_sessions_info: list = Db.get_all_session_info()
    all_sessions: list[SessionData] = []
    for session in all_sessions_info:
        session_data = SessionData(
            session[4], session[5], session[6], session[3], session[2], session[1]
        ).to_dict()
        all_sessions.append(session_data)
    print("All sessions =>", all_sessions)
    return all_sessions


@app.get("/get_total_spent_time")
async def get_total_spent_time():
    sessions = Db.calculate_total_spent_time()
    time_tree = time_tree_converter(sessions)

    # Convert defaultdict to dict for easier readability
    
    return time_tree



# Post requests


@app.post("/insert_session_info")
async def insert_session_info(req: Request, data: SessionModel):

    # Splitting titles based on " - " delimiter
    title_parts = [s.strip() for s in reverse_and_split_title(data.title).split("-")]
    while len(title_parts) < 3:
        title_parts.append("")

    mainTitle = title_parts[0]
    subtitle1 = title_parts[1]
    subtitle2 = title_parts[2]
    import json
    Db.insert_session_info(
        data.spentTime,
        str(data.startTime),
        str(data.endTime),
        mainTitle,
        subtitle1,
        subtitle2,
    )
    all_sessions = Db.get_all_session_info()
    global time_tree  # Access the global time_tree
    last_session = Db.get_last_session()
    print(last_session)
    time_tree = time_tree_converter(last_session)

    return time_tree

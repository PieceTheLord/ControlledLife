import time
from fastapi import FastAPI
from .db.Db import Db


app = FastAPI()


# Get requests

@app.get('/get_last_title')
async def last_title():
  return Db.get_last_title()

@app.get('/get_total_time')
async def total_time():
  return Db.get_total_time()

# Post requests

@app.post('insert_session_info/{title}')
async def insert_session_info(title: str):
  time = time.now()
  print(time, title)
  
  # Db.insert_session_info(time, title)






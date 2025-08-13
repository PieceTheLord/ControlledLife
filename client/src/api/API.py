import requests

class clientAPI:
  
  
  def __init__(self):
    self.URL = "http://127.0.0.1:8000"
  
  def insert_new_session_info(self, title):
    """Insert a new window's title to the db"""
    requests.post(self.URL + "/insert_session_info", data={title})


cAPI = clientAPI()

cAPI.insert_new_session_info("test")
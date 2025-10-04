import requests
<<<<<<< HEAD
import datetime
from utils.serialize_timedelta import serialize_timedelta
import json


class clientAPI:
    def __init__(self):
        self.url = "http://127.0.0.1:8000"

    def insert_session_info(
        self,
        spentTime: datetime.timedelta,
        startTime: datetime.datetime,
        endTime: datetime.datetime,
        title: str,
    ):
        """
        Send the spent time and app's title to the server, which then go to the SQLite db
        """
        data = {
            "title": title,
            "spentTime": spentTime.total_seconds(),
            "startTime": startTime.isoformat(),
            "endTime": endTime.isoformat(),
        }
        req = requests.post(
            f"{self.url}/insert_session_info",
            json=data,
        )
        return req.json()

    def get_last_session(self):
        req = requests.get(f"{self.url}/get_last_session")
        req.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        print(f"Last session from API.py -> {req.json()}")
        return req.json()
    
    def get_all_session(self):
        req = requests.get(f"{self.url}/get_all_sessions")
        req.raise_for_status()
        print(f"All sessions from API.py -> {req.json()}")
        return req.json()
    
    def get_total_spent_time(self):
        req = requests.get(f"{self.url}/get_total_spent_time")
        req.raise_for_status()
        print(f"Total spent time from API.py -> {req.json()}")
        return req.json()


API = clientAPI()
=======

class clientAPI:
  
  
  def __init__(self):
    self.URL = "http://127.0.0.1:8000"
  
  def insert_new_session_info(self, title):
    """Insert a new window's title to the db"""
    requests.post(self.URL + "/insert_session_info", data={title})


cAPI = clientAPI()

cAPI.insert_new_session_info("test")
>>>>>>> 0a51e5a2ef0724a6320866d08a2581e0b51640a7

import requests
import datetime
from utils.serialize_timedelta import serialize_timedelta

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
            "spentTime": serialize_timedelta(spentTime),
            "startTime": startTime.isoformat(),
            "endTime": endTime.isoformat()
        }
        req = requests.post(
            f"{self.url}/insert_session_info",
            json=data,
        )
        return req.json()


API = clientAPI()

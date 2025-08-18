import requests
import datetime

class clientAPI:
    def __init__(self):
        self.url = "http://127.0.0.1:8000"

    def insert_session_info(self, time: datetime.datetime, title: str):
        """
        Send the spent time and app's title to the server, which then go to the SQLite db
        """
        data = {"title": title, "time": time.isoformat()}
        req = requests.post(
            f"{self.url}/insert_session_info",
            json=data,
        )
        return req.json()


API = clientAPI()


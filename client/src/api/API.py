import requests
import json
import datetime


class clientAPI:
    def __init__(self):
        self.url = "http://127.0.0.1:8000"

    def insert_session_info(self, time: datetime.datetime, title: str):
        """
        Send the spent time and app's title to the server, which then go to the SQLite db
        """
        data = json.dumps({"title": title, "time": time}, default=str)
        req = requests.post(
            f"{self.url}/insert_session_info",
            json=data,
        )
        return req.json()


API = clientAPI()

# req = requests.post(
#     "http://127.0.0.1:8000/insert_session_info",
#     json={"title": "Maincraft", "time": str(time.time())},
# )
# print(req.json())

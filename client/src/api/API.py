import requests


class clientAPI:
    def __init__(self):
        self.url = "http://127.0.0.1:8000"

    def insert_session_info(self, time: str, title: str):
        """ "
        Send the spent time and app's title to the server, which then go to the SQLite db
        """
        requests.post(f"{self.url}/insert_session_info/{time}/{title}")


API = clientAPI()

class SessionData:
    def __init__(
        self,
        mainTitle: str,
        subtitle1: str,
        subtitle2: str,
        endTime: str,
        startTime: str,
        spentTime: str,
    ):
        self.mainTitle = mainTitle
        self.subtitle1 = {
            "title": subtitle1,
            "subtitle2": {
                "spentTime": spentTime,
                "title": subtitle2,
                "endTime": endTime,
                "startTime": startTime,
            },
        }

    def to_dict(self):
        return {
            "mainTitle": self.mainTitle,
            "subtitle1": {
                "title": self.subtitle1["title"],
                "subtitle2": {
                    "sepntTime": self.subtitle1["subtitle2"]["spentTime"],
                    "title": self.subtitle1["subtitle2"]["title"],
                    "endTime": self.subtitle1["subtitle2"]["endTime"],
                    "startTime": self.subtitle1["subtitle2"]["startTime"],
                },
            },
        }

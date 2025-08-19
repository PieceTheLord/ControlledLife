import datetime
from pydantic import BaseModel

class SessionModel(BaseModel):
    spentTime: str
    startTime: datetime.datetime
    endTime: datetime.datetime
    title: str

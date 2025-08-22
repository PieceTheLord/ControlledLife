import datetime
from pydantic import BaseModel

class SessionModel(BaseModel):
    spentTime: float
    startTime: datetime.datetime
    endTime: datetime.datetime
    title: str

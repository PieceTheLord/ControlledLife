import datetime
import json

def timedelta_to_iso_duration(td: datetime.timedelta) -> str:
    days = td.days
    seconds = td.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"P{days}DT{hours}H{minutes}M{seconds}S"

def serialize_timedelta(obj):
    if isinstance(obj, datetime.timedelta):
        return timedelta_to_iso_duration(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)
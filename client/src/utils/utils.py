import datetime

def time_split(input_string: datetime.datetime) -> str:
    """Divice the time by after and before the point for better looking"""
    return str(datetime.datetime.now() - input_string).split(".")[0]

import isodate


def ISO_parse(iso_str: str):
    """Convert timedelta type into ISO 8601 format"""
    return isodate.parse_duration(iso_str)

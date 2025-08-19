import re

def reverse_and_split_title(title: str) -> str:
    """
    Reverses a string, splits it by ' - ' using regex to avoid splitting within titles,
    and reassembles in reverse order.

    Args:
        title: The input string to process.

    Returns:
        A string with the parts reversed, or the original string if no valid delimiter is found.
    """
    parts = re.split(r"\s-\s", title)  # Split only at ' - ' with spaces around it
    if len(parts) == 1:
        return title # return the original title if there are no delimiters found
    parts.reverse()
    return " - ".join(parts)
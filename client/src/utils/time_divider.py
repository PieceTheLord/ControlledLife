import re

def parse_string(input_string):
  """Parses a string to extract the title and time.

  Args:
    input_string: A string in the format "title Time".

  Returns:
    A tuple containing the title (string) and time (string), 
    or None if the string does not match the expected format.
  """
  match = re.match(r"(.+)\s+(\d+:\d+:\d+)", input_string)
  if match:
    title = match.group(1)
    time_str = match.group(2)
    return title, time_str
  else:
    return "Can't parse time and title in utils.time_divider at parse_string function"
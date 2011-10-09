import re

compiled_regex = re.compile("#([a-zA-Z0-9\-\_]*)")
def get_hashtags_from_string(text):
  return compiled_regex.findall(text)




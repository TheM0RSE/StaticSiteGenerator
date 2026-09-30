import re

def extract_title(markdown: str):
    title = re.findall(r"^# (.*)", markdown)
    if title:
        return title[0].strip()
    else:
        raise Exception("Error: Found no h1 header")
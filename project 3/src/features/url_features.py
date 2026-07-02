import re


def contains_url(text: str) -> int:
    return int(bool(re.search(r"https?://|www\.", text)))

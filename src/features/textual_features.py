import re


def char_count(text: str) -> int:
    return len(text or "")


def word_count(text: str) -> int:
    return len(re.findall(r"\w+", text or ""))

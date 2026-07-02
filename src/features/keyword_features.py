import re


PHISHING_KEYWORDS = ["urgent", "click", "verify", "password", "bank", "invoice", "free"]


def keyword_count(text: str) -> int:
    lowered = text.lower()
    return sum(1 for keyword in PHISHING_KEYWORDS if keyword in lowered)

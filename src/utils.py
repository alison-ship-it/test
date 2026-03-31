"""Utility functions used across the application."""

import re
from collections import Counter


def is_valid_email(email):
    """Check whether a string looks like a valid email address."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return bool(re.match(pattern, email))


def clamp(value, low, high):
    """Clamp *value* so that low <= value <= high."""
    return max(low, min(high, value))


def word_frequencies(text):
    """Return a dict mapping each word (lower-cased) to its count."""
    words = re.findall(r"[a-zA-Z]+", text.lower())
    return dict(Counter(words))


def flatten(nested_list):
    """Flatten a list that may contain nested lists."""
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


def chunk(sequence, size):
    """Split *sequence* into chunks of *size*."""
    return [sequence[i : i + size] for i in range(0, len(sequence), size)]

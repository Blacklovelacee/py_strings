# pylint: disable=C0114

import re
import string


def reverse(text: str) -> str:
    """
    Return the 'text' backwards.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The text written backwards.
    """
    return text[::-1]


def first_to_upper(text: str) -> str:
    """
    Changes each first character of the word to uppercase.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    str
        The modified text
    """
    s = ''
    if len(text) > 0:
        s += text[0].upper()
        for i in range(1, len(text)):
            if text[i - 1] in string.punctuation \
            or text[i - 1] in string.whitespace:
                s += text[i].upper()
            else:
                s += text[i]

    return s


def count_vowels(text: str) -> int:
    """
    Counts number of vovels in the text.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    inp
        Number of vowels.
    """
    return len(re.findall(r'[AaEeYyUuIiOoąęóĄĘÓ]', text))

def sum_digits(text: str) -> int:
    """
    Finds all digitts in the text and returns its sum.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int
        Sum of all digits in the text.
    """
    return sum(map(int, re.findall(r'[1-9]', text)))


def search_substr(text: str, sub: str) -> int:
    """
    Search for sub(string) in the text. Returns the position or None.

    Parameters
    ----------
    text: str
        The input string

    Returns
    -------
    int or None
        Position of the sub(string) or None.
    """
    if text.find(sub) == -1:
        return None
    return text.find(sub)

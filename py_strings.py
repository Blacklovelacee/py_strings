# pylint: disable=C0114

import re

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
    s += text[0].upper()
    lib = {',', '.', ';', ':', ' ', '\n', '\t', '-'}
    if len(text) > 0:
      for i in range(1, len(text)):
         k = 0
         for sign in lib:
             if(text[i - 1] == sign):
                s += text[i].upper()
                k = 1
                break
         if k == 0:  
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
    s = 0
    for i in re.findall(r'[1-9]', text):
       s += int(i)
    
    return s


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

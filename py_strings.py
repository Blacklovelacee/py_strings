def reverse(text: str) -> str:
    return text[::-1]


def first_to_upper(text: str) -> str:
   s = ''
   s += text[0].upper()
   if len(text) > 0:
	   for i in range(1, len(text)):
   		if(text[i - 1] == ' '):
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
    pass


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
    pass


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
    pass

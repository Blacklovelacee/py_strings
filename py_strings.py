# pylint: disable=C0114

import re

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
    return len(re.findall(r'[A, a, E, e, Y, y, U, u, I, i, O, o]', text))

def sum_digits(text: str) -> int:
    s = 0
    for i in re.findall(r'[1-9]', text):
    	s += int(i)
    
    return s


def search_substr(text: str, sub: str) -> int:
    if text.find(sub) == -1:
    	return None
    else:
    	return text.find(sub)

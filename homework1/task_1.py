""" Написать метод domain_name, который вернет домен из url адреса. """

import re


def domain_name(url: str)->str:
    """Return domain name from url"""
    match = re.search(r'[./]?(?:www.)?\w+\-?\w+[.]', url)
    result = match[0]
    result = result.replace('www', '')
    result = result.replace('.', '')
    result = result.replace('/', '')
    return result

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"


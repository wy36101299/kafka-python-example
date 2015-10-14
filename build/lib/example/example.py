# -*- coding: utf-8

from __future__ import print_function

import requests  
from lxml import html


def get_title(url):  
    page = requests.get(url)
    root = html.fromstring(page.text)
    return root.findtext('.//title')


if __name__ == '__main__':  
    print(get_title('http://www.google.com/'))
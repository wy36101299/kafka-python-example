# -*- coding: utf-8 -*-

from example import example


def test_get_title():  
    result = example.get_title('http://www.google.com/')
    expect = 'Google'
    assert result == expect
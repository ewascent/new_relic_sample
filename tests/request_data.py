"""write test data"""
import requests
from requests import request
from urllib3.connectionpool import connection_from_url

_file = './data/some_words.txt'

def get_test_data(file):
    '''get test data and write it'''
    text_url = 'http://www.gutenberg.org/cache/epub/26884/pg26884.txt'
    http = connection_from_url(url=text_url)
    req = http.request(method='GET', url=text_url)
    raw_data = "".encode()

    if req.status == 200:
        raw_data = req.data
    else:
        i = 0
        while i < 500:
            raw_data = raw_data + ' '.encode() + get_words().encode()
            i += 1

    write_to_file(file=file, data=raw_data)

def get_words():
    '''getwords makes small sentances from a dict'''
    from random import randint
    words = {
        1: 'Python',  2: 'Finger', 3: 'Cup', 4: 'Napkin', 5: 'Running', 6: 'Elaborate', 7: 'Farming', 8: 'Kettlebell', 9: 'Freddo',
        10: 'Cartwheel', 11: 'Oscar', 12: 'Seal', 13: 'Farse', 14: 'Friggate', 15: 'Thumbnail', 16: 'Lamentations'
    }
    first = words[randint(1, 14)]
    second = words[randint(1, 14)]
    third = words[randint(1, 14)]

    return first + ' ' + second + ' ' + third + ' '

def write_to_file(file, data):
    '''write to file'''
    with open(file, 'wb') as _file:
        _file.seek(0)
        _file.truncate()
        _file.write(data)
    return _file

get_test_data(file=_file)

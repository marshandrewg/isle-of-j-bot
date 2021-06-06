import requests

"""Wrapper for jservice.io in Python including all api calls"""


base_url = 'jservice.io/api/'
def get_random(count):
    payload = {
        'count': count
    }
    resp = requests.get(f'{base_url}/random', params=payload).json
    return resp

def get_clues(value,category,min_date,max_date,offset):
    payload = {
        'value': value
        'category': category,
        'min_date': min_date,
        'max_date': max_date,
        'offset': offset
    }
    resp = requests.get(f'{baseurl}/clues', params=payload).json
    return resp

def get_categories(count, offset):
    payload = {
        'count': count,
        'offset': offset
    }
    resp = requests.get(f'{baseurl}/categories', params=payload).json

def get_category(id):
    payload = {
        'id': id,
    }
    resp = requests.get(f'{baseurl}/category', params=payload).json

def get_invalid(id):
    payload = {
        'id': id,
    }
    resp = requests.get(f'{baseurl}/invalid', params=payload).json
import requests

BASE_URL = "http://localhost:5000"


def get_page(path=''):
    return requests.get(BASE_URL + path)


def post_page(s, path=''):
    return requests.post(BASE_URL + path, data={'string': s})

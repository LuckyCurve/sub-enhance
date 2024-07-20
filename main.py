import urllib.parse


def string_encode(data):
    return urllib.parse.quote(data)

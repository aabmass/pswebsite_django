from urllib.parse import urlencode

def url_with_querystring(url, **kwargs):
    """
        Appends the kwargs as querystring style to the end of the
        url. e.g. url_with_querystring('/', arg=3) would return
        '/?arg=3'
    """
    return url + '?' + urlencode(kwargs)

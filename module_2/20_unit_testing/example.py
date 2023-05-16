import requests


def get_url_content():
    return requests.get("https://google.com")


def len_url_content():
    cont = get_url_content()
    return len(cont.text)

import requests
from time import perf_counter


def get_data(url):
    resp = requests.get(url)
    return resp.json()["name"]


def main():
    begin = perf_counter()
    characters = list()
    for i in range(1, 150):
        characters.append(get_data(f"https://rickandmortyapi.com/api/character/{i}"))

    for c in characters:
        print(c)
    print(f"Time taken is {perf_counter() - begin} seconds")


main()

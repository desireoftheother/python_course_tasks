import asyncio
import aiohttp
import requests

base_url = "https://rickandmortyapi.com/api/character"


async def get_last_page(session):
    response = await session.get(url=base_url).json()
    last_page = response["info"]["pages"]
    return last_page


async def get_pages_links(session):
    links = list()
    last_page = await get_last_page(session)
    for num in range(1, last_page + 1):
        page_url = base_url + f"/?page={num}"
        links.append(session.get(page_url))
    return links


async def get_data():
    characters = list()
    async with aiohttp.ClientSession() as session:
        tasks = get_pages_links(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            characters.append(await response.json())
    print(len(characters))
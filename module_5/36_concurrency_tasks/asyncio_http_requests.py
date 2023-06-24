import httpx
import asyncio
import logging

from aiolimiter import AsyncLimiter
from time import perf_counter
from typing import List, Awaitable


logging.basicConfig(level=logging.DEBUG, filename="async_http_logs.log", filemode="w")
logger = logging.getLogger("logger")


async def get_data(client: httpx.AsyncClient, url: str, limiter: AsyncLimiter):
    async with limiter:
        start: float = perf_counter()
        logger.info(msg=f"Sent request for url {url}")
        resp: httpx.Response = await client.get(url)
        logger.info(
            msg=f"Gor response for url {url}, time taken: {perf_counter() - start}"
        )
        return resp.json()["name"]


async def main():
    begin: float = perf_counter()
    async with httpx.AsyncClient() as client:
        limiter: AsyncLimiter = AsyncLimiter(150, 1)
        tasks: List[Awaitable] = list()
        for i in range(1, 150):
            tasks.append(
                get_data(
                    client, f"https://rickandmortyapi.com/api/character/{i}", limiter
                )
            )

        characters: List[str] = await asyncio.gather(*tasks)
        for c in characters:
            print(c)
    print(f"Time taken is {perf_counter() - begin} seconds")


asyncio.run(main())

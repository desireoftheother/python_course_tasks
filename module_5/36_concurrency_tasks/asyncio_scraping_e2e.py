import asyncio
import httpx
from selectolax.parser import HTMLParser
from pydantic import BaseModel

from aiolimiter import AsyncLimiter
from typing import List, Dict, Any, Awaitable

URL: str = "http://books.toscrape.com/"

a = [
    True
]*10

class Book(BaseModel):
    name: str
    img_url: str
    price: float
    in_stock: bool
    rating: float
    description: str
    upc: str
    genre: str


async def parse_book_page(
    client: httpx.AsyncClient,
    limiter: AsyncLimiter,
    book_url: str,
):
    book_page: httpx.Response = await client.get(book_url)
    return book_url


async def parse_catalogue_page(
    client: httpx.AsyncClient, limiter: AsyncLimiter, page_url: str
) -> List[Awaitable]:
    cat_page: httpx.Response = await client.get(page_url)
    cat_page_html_parser: HTMLParser = HTMLParser(cat_page.text)
    urls_list: List[str] = []
    for node in cat_page_html_parser.css("ol.row"):
        for link in node.css("h3"):
            urls_list.extend(link.select("a").matches)
    return await asyncio.gather(*[
        asyncio.create_task(
            parse_book_page(client, limiter, url.attributes.get("href"))
        )
        for url in urls_list
    ])


async def main():
    async with httpx.AsyncClient(base_url=URL) as client:
        limiter: AsyncLimiter = AsyncLimiter(150, 1)
        tasks_list = [
            asyncio.create_task(
                parse_catalogue_page(
                    client=client, page_url=URL + f"catalogue/page-{i}.html", limiter=limiter
                )
            )
            for i in range(1, 61)
        ]
        return await asyncio.gather(*tasks_list)


print(len(asyncio.run(main())))

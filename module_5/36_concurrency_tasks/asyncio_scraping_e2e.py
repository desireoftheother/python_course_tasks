import asyncio
import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass
from urllib.parse import urljoin


URL: str = "http://books.toscrape.com/"

client: httpx.Client = httpx.Client()
resp = client.get(URL)
html = HTMLParser(resp.text)

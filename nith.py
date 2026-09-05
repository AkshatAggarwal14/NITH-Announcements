import time
from urllib.parse import urljoin

import aiohttp
from bs4 import BeautifulSoup

URL = "https://nith.ac.in/"

# Simple in-memory cache so Vercel serverless (warm instances) and local
# dev don't hammer the NITH site on every request. 10s is Vercel hobby limit.
_CACHE: dict = {"data": None, "ts": 0.0}
CACHE_TTL = 3600  # 1 hour


def _prettify(s: str) -> str:
    return " ".join(s.split()).strip()


async def get_announcements(url: str = URL, use_cache: bool = True) -> list:
    if use_cache and _CACHE["data"] is not None:
        if time.time() - _CACHE["ts"] < CACHE_TTL:
            return _CACHE["data"]

    timeout = aiohttp.ClientTimeout(total=15)
    headers = {"User-Agent": "nith-announcements-api/1.0"}
    async with aiohttp.ClientSession(timeout=timeout, headers=headers) as session:
        async with session.get(url) as resp:
            resp.raise_for_status()
            html_content = await resp.read()

    soup = BeautifulSoup(html_content, "html.parser")
    announcements = []
    for divtag in soup.find_all(
        "div", attrs={"class": "text-center padding30 main-feature-events"}
    ):
        h3 = divtag.find("h3")
        if h3 is None or _prettify(h3.get_text()) != "Announcements":
            continue
        for ultag in divtag.find_all("ul", attrs={"class": "allnithlinks"}):
            for litag in ultag.find_all("li"):
                a = litag.find("a")
                if a is None:
                    continue
                announcement = _prettify(a.get_text())
                link = _prettify(a.get("href", ""))
                # resolve relative links like "/uploads/..."
                if link:
                    link = urljoin(url, link)
                if not announcement:
                    continue
                announcements.append(
                    {"Announcement": announcement, "Link": link}
                )

    _CACHE["data"] = announcements
    _CACHE["ts"] = time.time()
    return announcements

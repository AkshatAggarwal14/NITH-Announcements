import aiohttp
from bs4 import BeautifulSoup


async def prettify(s: str):
    return (' '.join(s.split())).strip()


async def get_announcements(url: str) -> list:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as page:
            html_content = await page.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            announcements = []
            for divtag in soup.find_all('div', attrs={'class': 'text-center padding30 main-feature-events'}):
                if(divtag.h3.text == "Announcements"):
                    for ultag in divtag.find_all('ul', attrs={'class': 'allnithlinks'}):
                        for litag in ultag.find_all('li'):
                            announcement = await prettify(litag.text)
                            link = await prettify(litag.a['href'])
                            announcements.append({
                                "Announcement": announcement,
                                "Link": link
                            })
            page.close()
            return announcements

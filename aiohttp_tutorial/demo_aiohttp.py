
import time
import asyncio, aiohttp

class WebCrawler:
    def __init__(self):
        pass

    async def fetch(self, session, url):
        async with session.get(url) as response:
            # https://docs.aiohttp.org/en/stable/client_reference.html
            html_body = await response.text()
            print(html_body)
            print(response.status)
            print(response.headers)
            print(await response.read())
            # print(await response.json(encoding=None))

    async def run(self):
        async with aiohttp.ClientSession() as session:
            url_link = "https://example.com/"
            tasks = [self.fetch(session, url_link) for _ in range(10)]
            await asyncio.gather(*tasks)

if __name__ == "__main__":

    now = time.time()
    crawler = WebCrawler()
    asyncio.run(crawler.run())
    print(time.time() - now)

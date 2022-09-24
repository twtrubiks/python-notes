
import time
import asyncio, aiohttp

# ClientTimeout
# https://docs.aiohttp.org/en/stable/client_quickstart.html#aiohttp-client-timeouts

class WebCrawler:
    def __init__(self):
        pass

    async def fetch(self, session, url):
        try:
            async with session.get(url) as response:
                html_body = await response.text()
        except asyncio.TimeoutError as e:
            print('timeout')

    async def run(self):
        timeout = aiohttp.ClientTimeout(total=0.00001)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            url_link = "https://example.com/"
            tasks = [self.fetch(session, url_link) for _ in range(10)]
            await asyncio.gather(*tasks)

if __name__ == "__main__":

    now = time.time()
    crawler = WebCrawler()
    asyncio.run(crawler.run())
    print(time.time() - now)


import time
import asyncio, aiohttp

# https://docs.python.org/3/library/asyncio-sync.html#asyncio.Semaphore
# https://stackoverflow.com/questions/55918048/asyncio-semaphore-runtimeerror-task-got-future-attached-to-a-different-loop

class WebCrawler:
    def __init__(self):
        pass

    async def fetch(self, session, url, semaphore):
        async with semaphore:
            async with session.get(url) as response:
                html_body = await response.text()
                print(html_body)

    async def run(self):
        async with aiohttp.ClientSession() as session:
            semaphore = asyncio.Semaphore(2)
            url_link = "https://example.com/"
            tasks = [self.fetch(session, url_link, semaphore) for _ in range(10)]
            await asyncio.gather(*tasks)

if __name__ == "__main__":

    now = time.time()
    crawler = WebCrawler()
    asyncio.run(crawler.run())
    print(time.time() - now)

import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1280, "height": 800})
        await page.goto("http://localhost:8000/index.html")
        await page.screenshot(path="verification/desktop_final.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())

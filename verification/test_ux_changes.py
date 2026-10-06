import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1280, "height": 800})

        # Verify index.html aria-current="page"
        await page.goto("http://localhost:8000/index.html")
        header_logo_aria = await page.get_attribute("header .logo", "aria-current")
        footer_logo_aria = await page.get_attribute("footer .footer-logo", "aria-current")
        print(f"Index header logo aria-current: {header_logo_aria}")
        print(f"Index footer logo aria-current: {footer_logo_aria}")
        assert header_logo_aria == "page"
        assert footer_logo_aria == "page"

        # Verify recipe.html Back to Top link target
        await page.goto("http://localhost:8000/recipe.html")
        back_to_top_href = await page.get_attribute("footer a[aria-label='Back to top']", "href")
        print(f"Recipe Back to Top href: {back_to_top_href}")
        assert back_to_top_href == "#recipe"

        # Scroll down to footer and click Back to Top
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(1.0)
        scroll_y_before = await page.evaluate("window.scrollY")
        print(f"Scroll Y before clicking: {scroll_y_before}")

        await page.click("footer a[aria-label='Back to top']")
        await asyncio.sleep(2.0)

        scroll_y = await page.evaluate("window.scrollY")
        print(f"Scroll Y position after clicking Back to Top: {scroll_y}")

        await page.screenshot(path="verification/verification_screenshot.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())

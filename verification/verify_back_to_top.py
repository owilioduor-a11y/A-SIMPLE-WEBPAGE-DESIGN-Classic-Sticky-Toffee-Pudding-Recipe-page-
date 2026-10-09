import asyncio
import os
import http.server
import socketserver
import threading
from playwright.async_api import async_playwright

PORT = 8085

def run_server():
    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

async def main():
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    await asyncio.sleep(1)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1280, "height": 800})

        await page.goto(f"http://localhost:{PORT}/recipe.html")
        await asyncio.sleep(0.5)

        # Force reveal active for animations
        await page.evaluate("""
            document.querySelectorAll('.reveal').forEach(el => {
                el.classList.add('active');
                el.style.transition = 'none';
            });
        """)

        # Scroll to bottom to footer
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(0.5)

        # Find back to top link
        back_to_top = page.locator("a[aria-label='Back to top']")
        href = await back_to_top.get_attribute("href")
        print(f"'Back to top' href attribute: {href}")
        assert href == "#recipe", f"Expected #recipe, got {href}"

        # Click back to top
        await back_to_top.click()
        await asyncio.sleep(1)

        # Verify scroll position is near top
        scroll_y = await page.evaluate("window.scrollY")
        print(f"Scroll Y after clicking 'Back to top': {scroll_y}")
        assert scroll_y < 100, f"Expected scroll Y near 0, got {scroll_y}"

        # Take screenshot
        os.makedirs("verification", exist_ok=True)
        screenshot_path = "verification/back_to_top_verified.png"
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())

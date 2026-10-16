import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Set mobile viewport
        context = await browser.new_context(viewport={"width": 375, "height": 667})
        page = await context.new_page()

        await page.goto("http://localhost:8000/index.html")

        # Force reveal active state so elements aren't obscured
        await page.evaluate("""() => {
            document.querySelectorAll('.reveal').forEach(el => {
                el.classList.add('active');
                el.style.transition = 'none';
            });
        }""")

        mobile_menu = page.locator("#mobile-menu")
        nav_list = page.locator("#nav-list")

        # Open mobile menu by dispatching click or clicking
        await mobile_menu.dispatch_event("click")
        await page.wait_for_timeout(300)

        # Check menu is active
        is_active = await mobile_menu.evaluate("el => el.classList.contains('active')")
        print("Menu active after click:", is_active)

        # Take screenshot of open menu
        await page.screenshot(path="/home/jules/verification/mobile_menu_open.png")

        # Press Escape key
        await page.keyboard.press("Escape")
        await page.wait_for_timeout(300)

        # Check menu is closed and focused
        is_closed = not (await mobile_menu.evaluate("el => el.classList.contains('active')"))
        aria_expanded = await mobile_menu.get_attribute("aria-expanded")
        is_focused = await mobile_menu.evaluate("el => document.activeElement === el")

        print("Menu closed after Escape:", is_closed)
        print("aria-expanded after Escape:", aria_expanded)
        print("Mobile menu is focused after Escape:", is_focused)

        # Take screenshot after Escape
        await page.screenshot(path="/home/jules/verification/mobile_menu_closed_escape.png")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())

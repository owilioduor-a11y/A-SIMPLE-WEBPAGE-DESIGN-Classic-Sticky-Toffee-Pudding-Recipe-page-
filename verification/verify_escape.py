import os
import glob
from playwright.sync_api import sync_playwright

def run_cuj(page):
    page.goto("http://localhost:8000/index.html")
    page.wait_for_timeout(500)

    # Open menu via dispatch_event to bypass small viewport touch/visibility constraints if any
    menu_btn = page.locator("#mobile-menu")
    menu_btn.dispatch_event("click")
    page.wait_for_timeout(800)

    # Press Escape key to close menu and focus button
    page.keyboard.press("Escape")
    page.wait_for_timeout(800)

    # Take screenshot at the key moment showing menu toggled closed and focus on button
    os.makedirs("/home/jules/verification/screenshots", exist_ok=True)
    page.screenshot(path="/home/jules/verification/screenshots/escape_dismissal.png")
    page.wait_for_timeout(1000)

if __name__ == "__main__":
    os.makedirs("/home/jules/verification/videos", exist_ok=True)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={"width": 375, "height": 667},
            record_video_dir="/home/jules/verification/videos"
        )
        page = context.new_page()
        try:
            run_cuj(page)
        finally:
            context.close()
            browser.close()

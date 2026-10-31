import os, time
from playwright.sync_api import sync_playwright, expect

def verify_back_to_top():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        file_path = os.path.abspath("recipe.html")
        page.goto(f"file://{file_path}")

        # Scroll down to footer
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # Click "Back to Top" link in footer
        back_to_top_link = page.get_by_role("link", name="Back to top")
        expect(back_to_top_link).to_be_visible()
        back_to_top_link.click()

        # Wait for smooth scroll to finish
        time.sleep(1)

        # Verify URL hash is #recipe
        expect(page).to_have_url(f"file://{file_path}#recipe")

        # Take screenshot of page top
        page.screenshot(path="/home/jules/verification/recipe_top_scroll.png")
        print("window.scrollY:", page.evaluate("window.scrollY"))
        browser.close()

if __name__ == "__main__":
    verify_back_to_top()

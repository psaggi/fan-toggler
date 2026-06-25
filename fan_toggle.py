"""
fan_toggle.py
Toggles the "Fan" smart plug on alexa.amazon.com.
"""

import os
import sys
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROFILE_DIR = os.path.join(SCRIPT_DIR, "chrome_profile")


def toggle_fan():
    with sync_playwright() as p:

        ctx = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            executable_path=CHROME_PATH,
            headless=False,
            args=["--start-maximized"],
            no_viewport=True,
        )

        page = ctx.new_page()

        try:
            page.goto("https://alexa.amazon.com", wait_until="domcontentloaded")

            if "signin" in page.url or "ap/signin" in page.url:
                print("First run: please log into Amazon in the Chrome window.")
                page.wait_for_url("https://alexa.amazon.com/**", timeout=120_000)

            page.wait_for_selector("button[aria-label='Smart Home']", timeout=15_000)
            page.evaluate("document.querySelector(\"button[aria-label='Smart Home']\").click()")

            page.wait_for_selector("text=Fan", timeout=15_000)
            page.wait_for_timeout(1000)

            fan_box = page.locator("text=Fan").first.bounding_box()
            page.mouse.click(fan_box["x"] + 10, fan_box["y"] + 50)
            page.wait_for_timeout(1500)

        except PlaywrightTimeout as e:
            print(f"Error: {e}")
            sys.exit(1)

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

        finally:
            ctx.close()


if __name__ == "__main__":
    toggle_fan()

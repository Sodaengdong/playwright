#콘솔 로그 캡처

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    # 브라우저 콘솔 로그 캡처
    page.on("console", lambda msg : print(f"[{msg.type}] :", msg.text))
    page.goto("https://practice.expandtesting.com/console-log")

    browser.close()
    
# 스크린샷 캡처

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://the-internet.herokuapp.com/")
    page.screenshot(path="screenshot.png") # 페이지 전체
    
    browser.close()

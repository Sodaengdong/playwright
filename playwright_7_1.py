# 로그인 폼 자동화 더 간단한 코드로 짜기
from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://the-internet.herokuapp.com/login")
    
    page.fill("#username", "tomsmith")
    page.fill("#password", "SuperSecretPassword!")
    
    page.locator(".radius").click()
    page.wait_for_timeout(10000) # 10초 대기
    print(page.locator("div#flash").text_content().strip()) # 공백 제거 후 출력
                        
    browser.close()  
# 동적 요소/지연 응답 대기 (wait_for_selector, timeout)

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://the-internet.herokuapp.com/dynamic_loading/2")
    
    page.get_by_role("button", name = "Start").click()
    page.wait_for_selector("text = Hello World!")
    
    print(page.inner_text("#finish")) #finish 요소의 텍스트를 즉시 읽어서 출력
    
    page.wait_for_timeout(3000) # 3초 대기
    
    browser.close()
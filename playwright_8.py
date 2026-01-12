# 체크박스 제어
from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://the-internet.herokuapp.com/checkboxes")
    
    #checkbox1 = page.locator("#checkboxes > input[type=checkbox]:nth-child(1)")
    #checkbox2 = page.locator("#checkboxes > input[type=checkbox]:nth-child(3)")
    
    checkbox1 = page.locator("#checkboxes input[type = 'checkbox']").nth(0)
    checkbox2 = page.locator("#checkboxes input[type = 'checkbox']").nth(1)
    
    checkbox1.check() # uncheck > check
    checkbox2.uncheck() # check > uncheck
    
    page.wait_for_timeout(5000) # 5초 대기
    
    print("checkbox1 : ", checkbox1.is_checked())
    print("checkbox2 : ", checkbox2.is_checked())
    
    browser.close()
    

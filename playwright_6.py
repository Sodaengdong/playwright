# 특정 버튼이 페이지에 존재하는지, 입력 필드가 활성화 상태인지 확인하는 테스트 작성하기
from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://the-internet.herokuapp.com/dynamic_controls")
    
    button = page.get_by_role("button", name="Remove")
    
    if button.count() > 0 : 
        print ("Remove 버튼 존재!!")
    
    else : 
        print ("Remove 버튼 미존재")
        
    inputbox = page.locator("#input-example > input")
    
    print("활성화 상태 : ", inputbox.is_enabled())
    print("비활성화 상태 : ", inputbox.is_disabled())
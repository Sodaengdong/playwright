# 셀렉트박스 제어
from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://the-internet.herokuapp.com/dropdown")
    
    # label로 선택
    page.select_option("#dropdown", label= "Option 1") # 첫번째 선택
    
    # value로 선택
    dropdown = page.locator("#dropdown").select_option("2") # 두번째 선택
    
    # 인덱스로 선택
    page.select_option("#dropdown", index=1) # 첫번째 선택
    
    
    browser.close()
    
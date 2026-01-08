# 버튼 클릭, 텍스트 입력, 드롭다운 선택 등 테스트 작성하기
from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://www.naver.com/")
    
    #print(page.locator("div#inputWrapper > input#input.truncate").count()) # count()로 선택자 존재 확인하기
    page.locator("input#query").click()
    page.locator("input#query").fill("playwright 공부")
    page.locator("svg#search-btn").click()
    
    page.wait_for_timeout(5000)
    # page.wait_for_selector("text=playwright") #playwright이란 텍스트가 보일 때 까지 기다리기
    
    browser.close()
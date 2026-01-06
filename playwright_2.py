# launch 메서드에 headless=True 옵션 사용하여 브라우저 백그라운드에서 실행하기

from playwright.sync_api import Playwright, sync_playwright, expect

# Playwright 실행

with sync_playwright() as p :
    # Chromium 브라우저 시작
    browser = p.chromium.launch(headless=True) # headless = True가 기본값이라 작성하지 않아도 됨, 브라우저 창 뜨지 않고 백그라운드에서만 실행됨 
    page = browser.new_page()
    
    
    # 페이지 이동
    page.goto("https://www.google.com/")
    print("Page Title : ", page.title()) # 페이지 제목 출력
    
    # 브라우저 종료
    browser.close()
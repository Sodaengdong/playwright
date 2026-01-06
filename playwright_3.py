#Firefox로 브라우저로 실행하기

from playwright.sync_api import Playwright, sync_playwright, expect

# Playwright 실행

with sync_playwright() as p :  # Playwright 실행과 종료를 자동으로 관리하는 컨텍스트 문
    # Firefox 브라우저 시작
    browser = p.firefox.launch(headless=False, slow_mo=100) # slow_mo : 각 Playwright 동작 사이마다 100밀리초(ms)씩 지연, 눈으로 확인 가능
    page = browser.new_page()
    
    
    # 페이지 이동
    page.goto("https://www.google.com/")
    print("Page Title : ", page.title()) # 페이지 제목 출력
    
    # 브라우저 종료
    browser.close()
    

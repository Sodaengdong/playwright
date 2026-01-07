# ID, Class, CSS, XPath 등 선택자를 사용하여 HTML 요소 선택하고 출력하기

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p : 
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    page.goto("https://books.toscrape.com/")
    
    # h1 : HTML 태그 이름, 태그 자체 선택자
    element1 = page.locator("h1")
    print("h1 : " + element1.text_content())
    
    # class
    element2 = page.locator(".form-horizontal")
    print("class : " + element2.text_content().strip()) #strip 사용하여 앞뒤의 \n, 공백 제거 후 문자열만 출력
    
    # css
    element3 = page.locator("div.alert.alert-warning")
    print("CSS : " + element3.text_content())

    browser.close()

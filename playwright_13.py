# 파일 업로드

from playwright.sync_api import Playwright, sync_playwright, expect

with sync_playwright() as p :
    
    browser = p.chromium.launch(headless=False, slow_mo=300)
    page = browser.new_page()
    
    page.goto("https://the-internet.herokuapp.com/upload")
    
    upload = page.locator("input#file-upload")
    upload.set_input_files("C:/Users/Administrator/Downloads/test.jfif")
    upload.set_input_files([]) # 업로드 취소, 초기화
    upload.set_input_files("C:/Users/Administrator/Downloads/test.jfif") # 재업로드
    
    page.locator("input.button").click()
    
    expect(page.get_by_text("test.jfif")).to_be_visible()
    print(page.inner_text("#uploaded-files"))
    page.wait_for_timeout(5000)
    
    browser.close()

    
     
    
    


# Playwright_codegen으로 자동 생성된 테스트 코드

import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.naver.com/")
    page.get_by_role("combobox", name="검색어를 입력해 주세요").press("CapsLock")
    page.get_by_role("combobox", name="검색어를 입력해 주세요").fill("Playwright selenium 비교")
    page.get_by_role("button", name="검색", exact=True).click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="Playwright, Selenium, Cypress").first.click()
    page1 = page1_info.value

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

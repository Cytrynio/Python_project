import pytest
from selenium import webdriver
from main import LoginPage
from time import sleep

def test_login_page():
    driver = webdriver.chrome()
    page = LoginPage(driver)
    page.open()
    page.print_page_info()
    page.enter_username('standard_user')
    page.enter_password('secret_sauce')
    page.click_login()
    sleep(1)
    page.print_page_info()
    try:
        assert page.get_current_url() == page.after_login_url
    except AssertionError:
        print('Assercja nie przeszła')
        raise
    else:
        print('Assercja przeszła')
    finally:
        print('Po asercji')
        driver.quit()
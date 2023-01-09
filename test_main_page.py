from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser,link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
    login = LoginPage(browser, browser.current_url)
    login.should_be_login_url()
    login.should_be_login_form()
    login.should_be_register_form()


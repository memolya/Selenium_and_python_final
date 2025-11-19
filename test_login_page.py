from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_guest_can_go_to_login_page_and_see_login_page(browser):
    main_link = "http://selenium1py.pythonanywhere.com/"

    # Гость открывает главную страницу
    main_page = MainPage(browser, main_link)
    main_page.open()

    # Переходит по ссылке логина
    main_page.go_to_login_page()

    # Создаём PageObject для страницы логина
    login_page = LoginPage(browser, browser.current_url)

    # Проверяем, что это действительно страница логина
    login_page.should_be_login_page()


def test_login_form_is_present(browser):
    login_page = LoginPage(browser, browser.current_url)
    login_page.open()
    login_page.should_be_login_form()

def test_register_form_is_present(browser):
    login_page = LoginPage(browser, browser.current_url)
    login_page.open()
    login_page.should_be_register_form()





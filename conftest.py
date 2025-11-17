import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="UI language, e.g. --language=es / fr / ru / en"
    )

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    yield driver
    print("\nquit browser..")
    driver.quit()
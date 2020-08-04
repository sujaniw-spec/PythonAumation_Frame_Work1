import pytest
import selenium


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser command line")


@pytest.fixture(scope='class')  # run before all the test
def test_setup(request):
    from selenium import webdriver
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Python38/chromedriver.exe")
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path="C:/Python38/geckodriver.exe")

    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield  # run after all the tests
    driver.close()
    driver.quit()
    # x = driver.title
    print("Test Completed")

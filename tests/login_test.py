import allure
import moment
import pytest

from pages.homePage import HomePage
from pages.loginPage import LoginPage
from utils import utils


@pytest.mark.usefixtures("test_setup")


class TestLogin():

    # @pytest.fixture(scope='session') #run before all the test

    def test_login(self):
        #driver.get("https://opensource-demo.orangehrmlive.com")
        driver = self.driver
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()
        # driver.find_element_by_id("txtUsername").send_keys("Admin")
        # driver.find_element_by_id("txtPassword").send_keys("admin123")
        # driver.find_element_by_id("btnLogin").click()

    def test_logout(self):
        try:
            driver = self.driver
            logout = HomePage(driver)
            logout.click_welcome()
            logout.click_logout()
            x = driver.title
            assert x == "OrangeHRM"
        except AssertionError as error:
            print("Assertion error has occurred")
            print(error)
            currentTime = moment.now().strftime("%H-%M-%S_%d-%m-%y")
            testname = utils.whoami()
            screenshotname = testname+"_"+currentTime
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshotname,
            attachment_type=allure.attachment_type.PNG)
            driver.get_screenshot_as_file("C:/Users/sujan/PycharmProjects/POM-Projects/Aumation_Frame_Work1/screenshots/"+screenshotname+".jpg")
            raise
        except:
            print("There was as exception")
            raise
        else:
            print("No exception occure")
        finally:
            print("I am inside the finally block")

            # driver.find_element_by_id("welcome").click()
        # driver.find_element_by_link_text("Logout").click()

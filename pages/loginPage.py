from selenium import webdriver
import pytest


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_text_box_id = "txtUsername"
        self.password_text_box_id = "txtPassword"
        self.login_button_id = "btnLogin"

        self.welcome_link_id = "welcome"
        self.linkText = "Logout"

    def enter_username(self, username):
        self.driver.find_element_by_id(self.username_text_box_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_id(self.password_text_box_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_id(self.login_button_id).click()

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_id(self.linkText).click()


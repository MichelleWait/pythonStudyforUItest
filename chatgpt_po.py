# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/29 21:32
@Auth ： michelle
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.XPATH, '//*[@id="TANGRAM__PSP_10__userName"]')
        self.password_input = (By.XPATH, '//*[@id="TANGRAM__PSP_10__password"]')
        self.submit_button = (By.XPATH, '//*[@id="TANGRAM__PSP_10__submit"]')

    def login(self, username, password):
        username_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_input)
        )
        password_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_input)
        )
        submit_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.submit_button)
        )

        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.login_button = (By.XPATH, '//*[@id="s-top-loginbtn"]')

    def go_to_login_page(self):
        login_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_button.click()
        return LoginPage(self.driver)

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_baidu_login(browser):
    browser.get("https://www.baidu.com/")
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login("your_username", "your_password")
    # Add assertions to verify the login was successful




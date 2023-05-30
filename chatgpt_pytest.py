# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/29 21:33
@Auth ： michelle
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_baidu_login(browser):
    browser.get("https://www.baidu.com/")

    login_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="s-top-loginbtn"]'))
    )
    login_button.click()

    username_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="TANGRAM__PSP_10__userName"]'))
    )
    password_input = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="TANGRAM__PSP_10__password"]'))
    )

    # Replace with your actual username and password
    username_input.send_keys("your_username")
    password_input.send_keys("your_password")

    submit_button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="TANGRAM__PSP_10__submit"]'))
    )
    submit_button.click()

    # Add assertions to verify the login was successful

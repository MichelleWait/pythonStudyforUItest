# -*- coding: utf-8 -*-
"""
@Time ： 2023/5/29 21:27
@Auth ： michelle
"""

import pytest
from selenium import webdriver
import time


@pytest.fixture(scope="module")
def browser():
    print("hello world")
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def test_shousuo(browser):
    browser.get('https://www.baidu.com')

    browser.find_element("id", "kw").send_keys("哈哈")

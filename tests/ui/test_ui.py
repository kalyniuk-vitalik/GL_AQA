import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


@pytest.mark.ui
def test_check_incorrect_username():
    driver = webdriver.Chrome()
    driver.get("https://github.com/login")
    login_elem = driver.find_element(By.ID, "login_field")
    login_elem.send_keys("vitalik1802@gmail.com")
    password_elem = driver.find_element(By.ID, "password")
    password_elem.send_keys("jv8eru93hvi3rhfr3")
    signin_elem = driver.find_element(By.NAME, "commit")
    signin_elem.click()
    alert_pass_or_login_message = driver.find_element(By.CLASS_NAME, 'js-flash-alert')
    assert driver.title == "Sign in to GitHub · GitHub"
    assert alert_pass_or_login_message.text == "Incorrect username or password."
    driver.close()

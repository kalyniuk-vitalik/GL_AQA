from module.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"

    def __init__(self):
        super().__init__()

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def try_login(self, username, password):
        login_elem = self.driver.find_element(By.ID, "login_field")
        login_elem.send_keys(username)

        pass_elem = self.driver.find_element(By.ID, "password")
        pass_elem.send_keys(password)

        signin_elem = self.driver.find_element(By.NAME, "commit")
        signin_elem.click()

    def check_title(self, expected_title):
        return self.driver.title == expected_title

    def check_alert_message(self, expected_message):
        return self.driver.find_element(By.CLASS_NAME, 'js-flash-alert').text == expected_message

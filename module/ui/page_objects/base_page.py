from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    DRIVER_NAME = "chromedriver"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def accept_cookie(self):
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, ".btn.btn--primary.CookiesInfo__cookiesInfoBtnWrapperAccept__nyIJU")))
            cookie_button.click()
        except NoSuchElementException:
            return False

    def close(self):
        self.driver.close()

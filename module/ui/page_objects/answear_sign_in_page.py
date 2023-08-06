from module.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignInPage(BasePage):
    URL = "https://answear.ua/mii-akkaunt/uviity"

    def __init__(self):
        super().__init__()
        self.wait = WebDriverWait(self.driver, 10)

    def go_to(self):
        self.driver.get(SignInPage.URL)

    def accept_cookie_sign_in_page(self):
        self.accept_cookie()

    def try_to_create_account(self, mail, password):
        mail_field = self.driver.find_element(By.ID, "email")
        mail_field.send_keys(mail)

        password_field = self.driver.find_element(By.ID, "plaintextPassword")
        password_field.send_keys(password)

    def accept_checkbox(self, checkbox):
        checkbox_element = self.driver.find_element(By.ID, checkbox)
        self.driver.execute_script("arguments[0].click();", checkbox_element)

    def click_create_account(self):
        create_acc_element = self.driver.find_element(By.CSS_SELECTOR, ".btn.xs-12.l-12.btn--primary.btn--fluid.RegisterStepForm__submitButton__Ao-fl")
        create_acc_element.click()

    def check_title(self, expected_title):
        return self.wait.until(EC.title_is(expected_title))

    def check_invalid_email_error_message(self, error_message):
        message = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".fieldError.FieldError__error__ZiVkd"))).text
        if message == error_message:
            return True
        else:
            return False

    def sign_in_exciting_user(self, mail, password):
        mail_field = self.driver.find_element(By.ID, "_username")
        mail_field.send_keys(mail)

        password_field = self.driver.find_element(By.ID, "_password")
        password_field.send_keys(password)

    def click_sign_in(self):
        create_acc_element = self.driver.find_element(By.CSS_SELECTOR, ".btn.xs-12.l-12.btn--primary.btn--fluid")
        create_acc_element.click()

    def click_add_data_to_new_user(self):
        add_data_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn.btn--default.DeliveryAddresses__deliveryAddressesButton__DyPxa")))
        add_data_button.click()

    def fill_in_the_required_fields(self, name, surname, last_name, street, house_number, postal_code, region, city, phone):
        fill_name = self.driver.find_element(By.ID, "userFirstName")
        fill_name.send_keys(name)

        fill_surname = self.driver.find_element(By.ID, "patronymic")
        fill_surname.send_keys(surname)

        fill_last_name = self.driver.find_element(By.ID, "userSurname")
        fill_last_name.send_keys(last_name)

        fill_street = self.driver.find_element(By.ID, "street")
        fill_street.send_keys(street)

        fill_house_number = self.driver.find_element(By.ID, "houseNumber")
        fill_house_number.send_keys(house_number)

        fill_postal_code = self.driver.find_element(By.ID, "postalCode")
        fill_postal_code.send_keys(postal_code)

        fill_region = self.driver.find_element(By.ID, "region")
        fill_region.send_keys(region)

        fill_city = self.driver.find_element(By.ID, "city")
        fill_city.send_keys(city)

        fill_phone = self.driver.find_element(By.ID, "phone")
        fill_phone.send_keys(phone)

        save_button = self.driver.find_element(By.CSS_SELECTOR, ".btn.btn--primary.btn--wide-medium.FormSubmitterContent__button__oZ3Fa")
        save_button.click()

    def check_new_data_message(self, error_message):
        message = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".Notification__notificationTitle__FAcpM"))).text
        if message == error_message:
            return True
        else:
            return False

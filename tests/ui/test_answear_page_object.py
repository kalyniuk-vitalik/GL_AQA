from module.ui.page_objects.answear_sign_in_page import SignInPage
import pytest
import time


@pytest.mark.ui
def test_registration_new_user():
    sign_in_page = SignInPage()
    sign_in_page.go_to()

    sign_in_page.accept_cookie_sign_in_page()
    # Should use only unregistered mail
    sign_in_page.try_to_create_account("test_answear18@yopmail.com", "jnnjkElFn&^cgsjd77")

    sign_in_page.accept_checkbox("agreement.terms_radio_0")
    sign_in_page.accept_checkbox("agreement.newsletter_radio_0")

    sign_in_page.click_create_account()

    assert sign_in_page.check_title("Дані акаунту | ANSWEAR.ua"), "New user is not registered"

@pytest.mark.ui
def test_sign_in():
    sign_in_page = SignInPage()
    sign_in_page.go_to()

    sign_in_page.accept_cookie_sign_in_page()
    # Should use only registered mail
    sign_in_page.sign_in_exciting_user("test_answear18@yopmail.com", "jnnjkElFn&^cgsjd77")

    sign_in_page.click_sign_in()

    assert sign_in_page.check_title("Дані акаунту | ANSWEAR.ua")

@pytest.mark.ui
def test_fill_user_data():
    sign_in_page = SignInPage()
    sign_in_page.go_to()

    sign_in_page.accept_cookie_sign_in_page()
    # Should use only registered mail
    sign_in_page.sign_in_exciting_user("test_answear18@yopmail.com", "jnnjkElFn&^cgsjd77")

    sign_in_page.click_sign_in()

    assert sign_in_page.check_title("Дані акаунту | ANSWEAR.ua")

    sign_in_page.click_add_data_to_new_user()
    sign_in_page.fill_in_the_required_fields("Віктор", "Степанович", "Шевченко", "Валова", 4, 43222, "Волинська", "Луцьк", 689545677)
    assert sign_in_page.check_new_data_message("Нова адреса додана")




@pytest.mark.ui
def test_registration_existing_user():
    sign_in_page = SignInPage()
    sign_in_page.go_to()

    sign_in_page.accept_cookie_sign_in_page()
    # Should use only registered mail
    sign_in_page.try_to_create_account("test_answearffbdbfbbbf8@yopmail.com", "jnnjkElFn&^cgsjd77")

    sign_in_page.accept_checkbox("agreement.terms_radio_0")
    sign_in_page.accept_checkbox("agreement.newsletter_radio_0")

    sign_in_page.click_create_account('.btn.xs-12.l-12.btn--primary.btn--fluid.RegisterStepForm__submitButton__Ao-fl')

    assert sign_in_page.check_invalid_email_error_message(
        "Зазначена адреса електронної пошти вже існує. Увійдіть в Акаунт або скористайтеся можливістю зміни пароля.")

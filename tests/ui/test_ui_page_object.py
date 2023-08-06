from module.ui.page_objects.github_sign_in_page import SignInPage
import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object():
    sign_in_page = SignInPage()
    sign_in_page.go_to()

    sign_in_page.try_login("vitalik1802@gmail.com", "qwfq")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")
    assert sign_in_page.check_alert_message("Incorrect username or password.")

    sign_in_page.close()

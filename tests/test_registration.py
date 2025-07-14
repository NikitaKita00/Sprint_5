import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import RegistrationLocators
from data.urls import Urls
from data.data import USER_PASSWORD, EXPECTED_USER_NAME
from helpers.helpers import generate_random_email


class TestRegistration:
    def test_successful_registration_and_avatar_display(self, browser):
        browser.get(Urls.MAIN_PAGE)

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.LOGIN_REGISTER_BUTTON)
        ).click()

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.NO_ACCOUNT_BUTTON)
        ).click()

        email = generate_random_email()
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.EMAIL_INPUT)
        )
        email_input.clear()
        email_input.send_keys(email)

        password_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.PASSWORD_INPUT)
        )
        password_input.clear()
        password_input.send_keys(USER_PASSWORD)

        repeat_password_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(RegistrationLocators.REPEAT_PASSWORD_INPUT)
        )
        repeat_password_input.clear()
        repeat_password_input.send_keys(USER_PASSWORD)

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(RegistrationLocators.CREATE_ACCOUNT_BUTTON)
        ).click()

        avatar_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(RegistrationLocators.AVATAR_BUTTON)
        )
        assert (
            avatar_button.is_displayed()
        ), "Аватар пользователя не отображается после регистрации"

        user_name_elem = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(RegistrationLocators.USER_NAME)
        )
        assert (
            user_name_elem.is_displayed()
        ), "Имя пользователя не отображается после регистрации"
        assert (
            user_name_elem.text.strip() == EXPECTED_USER_NAME
        ), f"Ожидалось имя '{EXPECTED_USER_NAME}', но получено '{user_name_elem.text.strip()}'"

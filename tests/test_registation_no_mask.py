import pytest
from data.urls import Urls
from locators.locators import RegistrationLocators
from helpers.helpers import (
    click_element,
    fill_input,
    assert_field_highlighted_red,
    assert_error_message_displayed,
)


class TestPasswordFieldsValidation:
    def test_password_fields_highlighted_red(self, browser):
        browser.get(Urls.MAIN_PAGE)

        click_element(browser, RegistrationLocators.LOGIN_REGISTER_BUTTON)
        click_element(browser, RegistrationLocators.NO_ACCOUNT_BUTTON)

        fill_input(
            browser, RegistrationLocators.EMAIL_INPUT, "йцвцйв"
        )  # Некорректный email

        click_element(browser, RegistrationLocators.CREATE_ACCOUNT_BUTTON)

        # Проверка Email
        assert_field_highlighted_red(
            browser,
            RegistrationLocators.EMAIL_INPUT,
            RegistrationLocators.EMAIL_ERROR_CONTAINER,
        )
        assert_error_message_displayed(
            browser, RegistrationLocators.EMAIL_ERROR_MESSAGE
        )

        # Проверка Пароля
        assert_field_highlighted_red(
            browser,
            RegistrationLocators.PASSWORD_INPUT,
            RegistrationLocators.PASSWORD_ERROR_CONTAINER,
        )

        # Проверка Повторите пароль
        assert_field_highlighted_red(
            browser,
            RegistrationLocators.REPEAT_PASSWORD_INPUT,
            RegistrationLocators.REPEAT_PASSWORD_ERROR_CONTAINER,
        )

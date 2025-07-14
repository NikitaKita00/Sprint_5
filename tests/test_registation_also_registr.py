import pytest
from data.urls import Urls
from data.data import EXISTING_USER_EMAIL, EXISTING_USER_PASSWORD
from locators.locators import RegistrationLocators
from helpers.helpers import (
    click_element,
    fill_input,
    assert_element_has_class,
    assert_element_displayed,
)


class TestRegistrationExistingUser:
    def test_registration_existing_user_shows_error(self, browser):
        browser.get(Urls.MAIN_PAGE)

        # Нажать кнопку "Вход и регистрация"
        click_element(browser, RegistrationLocators.LOGIN_REGISTER_BUTTON)

        # Нажать кнопку "Нет аккаунта"
        click_element(browser, RegistrationLocators.NO_ACCOUNT_BUTTON)

        # Заполнить поля Email, Пароль, Повторите пароль
        fill_input(browser, RegistrationLocators.EMAIL_INPUT, EXISTING_USER_EMAIL)
        fill_input(browser, RegistrationLocators.PASSWORD_INPUT, EXISTING_USER_PASSWORD)
        fill_input(
            browser, RegistrationLocators.REPEAT_PASSWORD_INPUT, EXISTING_USER_PASSWORD
        )

        # Нажать кнопку "Создать аккаунт"
        click_element(browser, RegistrationLocators.CREATE_ACCOUNT_BUTTON)

        # Проверка, что поля Email, Пароль, Повторите пароль выделены красным (наличие класса ошибки)
        assert_element_has_class(
            browser,
            RegistrationLocators.EMAIL_ERROR_CONTAINER,
            "input_inputError__fLUP9",
        )
        assert_element_has_class(
            browser,
            RegistrationLocators.PASSWORD_ERROR_CONTAINER,
            "input_inputError__fLUP9",
        )
        assert_element_has_class(
            browser,
            RegistrationLocators.REPEAT_PASSWORD_ERROR_CONTAINER,
            "input_inputError__fLUP9",
        )

        # Проверка, что под полем Email отображается сообщение «Ошибка»
        assert_element_displayed(browser, RegistrationLocators.EMAIL_ERROR_MESSAGE)

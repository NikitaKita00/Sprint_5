import pytest
from data.urls import Urls
from data.data import USER_EMAIL, USER_PASSWORD, EXPECTED_USER_NAME
from locators.locators import AuthLocators
from helpers.helpers import click_element, fill_input, wait_for_element


class TestLogin:
    def test_login_and_check_avatar_and_username(self, browser):
        # Открываем главную страницу
        browser.get(Urls.MAIN_PAGE)

        # Нажимаем кнопку "Вход и регистрация"
        click_element(browser, AuthLocators.LOGIN_REGISTER_BUTTON)

        # Вводим Email
        fill_input(browser, AuthLocators.EMAIL_INPUT, USER_EMAIL)

        # Вводим пароль
        fill_input(browser, AuthLocators.PASSWORD_INPUT, USER_PASSWORD)

        # Нажимаем кнопку "Войти"
        click_element(browser, AuthLocators.LOGIN_BUTTON)

        # Проверяем, что отображается аватар пользователя
        avatar_button = wait_for_element(browser, AuthLocators.USER_AVATAR)
        assert avatar_button.is_displayed(), "Аватар пользователя не отображается"

        # Проверяем, что отображается имя пользователя
        user_name_elem = wait_for_element(browser, AuthLocators.USER_NAME)
        assert user_name_elem.is_displayed(), "Имя пользователя не отображается"
        assert user_name_elem.text.strip() == EXPECTED_USER_NAME, \
            f"Ожидалось имя '{EXPECTED_USER_NAME}', но получено '{user_name_elem.text.strip()}'"

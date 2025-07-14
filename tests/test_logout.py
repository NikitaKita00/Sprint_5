import pytest
from data.urls import Urls
from data.data import USER_EMAIL, USER_PASSWORD
from locators.locators import AuthLocators
from helpers.helpers import click_element, fill_input, wait_for_element, wait_for_element_invisibility


class TestUserLogout:
    def test_logout_ui_elements(self, browser):
        # 1. Открываем главную страницу
        browser.get(Urls.MAIN_PAGE)

        # 2. Нажимаем "Вход и регистрация"
        click_element(browser, AuthLocators.LOGIN_REGISTER_BUTTON)

        # 3. Вводим учетные данные
        fill_input(browser, AuthLocators.EMAIL_INPUT, USER_EMAIL)
        fill_input(browser, AuthLocators.PASSWORD_INPUT, USER_PASSWORD)

        # 4. Нажимаем "Войти"
        click_element(browser, AuthLocators.LOGIN_BUTTON)

        # 5. Проверяем успешный вход — аватар отображается
        wait_for_element(browser, AuthLocators.USER_AVATAR, timeout=15)

        # 6. Нажимаем "Выйти"
        click_element(browser, AuthLocators.LOGOUT_BUTTON)

        # 7. Проверяем, что аватар и имя пользователя исчезли
        wait_for_element_invisibility(browser, AuthLocators.USER_AVATAR)

        # 8. Проверяем, что появилась кнопка "Вход и регистрация"
        wait_for_element(browser, AuthLocators.LOGIN_REGISTER_BUTTON)

        # 9. Дополнительно проверяем, что аватаров нет на странице
        avatar_elements = browser.find_elements(*AuthLocators.USER_AVATAR)
        assert len(avatar_elements) == 0, "Аватар пользователя отображается после выхода"

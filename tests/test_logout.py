import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import AuthLocators


class TestUserLogout:
    def test_logout_ui_elements(self, browser):
        # 1. Открываем главную страницу
        browser.get("https://qa-desk.stand.praktikum-services.ru/")

        # 2. Нажимаем "Вход и регистрация"
        login_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_REGISTER_BUTTON)
        )
        login_btn.click()

        # 3. Вводим учетные данные
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AuthLocators.EMAIL_INPUT)
        )
        email_input.send_keys("manya.nzenliv@gmail.com")

        password_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AuthLocators.PASSWORD_INPUT)
        )
        password_input.send_keys("Qwerty123!")

        # 4. Нажимаем "Войти"
        login_submit_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(AuthLocators.LOGIN_BUTTON)
        )
        login_submit_btn.click()

        # 5. Проверяем успешный вход
        WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(AuthLocators.USER_AVATAR)
        )

        # 6. Нажимаем "Выйти"
        logout_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(AuthLocators.LOGOUT_BUTTON)
        )
        logout_btn.click()

        # 7. Проверяем, что аватар и имя User исчезли
        WebDriverWait(browser, 10).until(
            EC.invisibility_of_element_located(AuthLocators.USER_AVATAR)
        )

        # 8. Проверяем, что появилась кнопка "Вход и регистрация"
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AuthLocators.LOGIN_REGISTER_BUTTON)
        )

        # 9. Дополнительная проверка
        avatar_elements = browser.find_elements(*AuthLocators.USER_AVATAR)
        assert len(avatar_elements) == 0

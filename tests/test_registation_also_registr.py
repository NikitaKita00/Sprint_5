import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestRegistrationExistingUser:
    def test_registration_existing_user_shows_error(self, browser):
        """
        Проверка регистрации с уже существующим пользователем:
        - Логин: manya.nzenliv@gmail.com
        - Пароль: qwe123qwe
        - Повтор пароля: qwe123qwe

        Ожидается, что поля Email, Пароль, Повторите пароль выделены красным,
        а под Email отображается сообщение «Ошибка».
        """
        browser.get("https://qa-desk.stand.praktikum-services.ru/")

        # Нажать кнопку "Вход и регистрация"
        login_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and contains(., 'Вход и регистрация')]",
                )
            )
        )
        login_btn.click()

        # Нажать кнопку "Нет аккаунта"
        no_account_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and contains(., 'Нет аккаунта')]",
                )
            )
        )
        no_account_btn.click()

        # Заполнить поля Email, Пароль, Повторите пароль
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        email_input.clear()
        email_input.send_keys("manya.nzenliv@gmail.com")

        password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.clear()
        password_input.send_keys("qwe123qwe")

        repeat_password_input = browser.find_element(
            By.CSS_SELECTOR, "input[name='submitPassword']"
        )
        repeat_password_input.clear()
        repeat_password_input.send_keys("qwe123qwe")

        # Нажать кнопку "Создать аккаунт"
        create_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonPrimary') and contains(., 'Создать аккаунт')]",
                )
            )
        )
        create_btn.click()

        # Проверка, что поля Email, Пароль, Повторите пароль выделены красным (наличие класса ошибки)
        email_field = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_container = email_field.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'input_inputError__fLUP9')]"
        )
        assert "input_inputError__fLUP9" in email_container.get_attribute(
            "class"
        ), "Поле Email должно быть выделено красным"

        password_container = password_input.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'input_inputError__fLUP9')]"
        )
        assert "input_inputError__fLUP9" in password_container.get_attribute(
            "class"
        ), "Поле Пароль должно быть выделено красным"

        repeat_password_container = repeat_password_input.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'input_inputError__fLUP9')]"
        )
        assert "input_inputError__fLUP9" in repeat_password_container.get_attribute(
            "class"
        ), "Поле Повторите пароль должно быть выделено красным"

        # Проверка, что под полем Email отображается сообщение «Ошибка»
        error_message_element = email_container.find_element(
            By.XPATH,
            "./ancestor::div[1]/following-sibling::span[contains(@class, 'input_span__yWPqB') and contains(text(), 'Ошибка')]",
        )
        assert (
            error_message_element.is_displayed()
        ), "Сообщение 'Ошибка' должно отображаться под полем Email"

import time
import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestRegistration:
    def generate_random_email(self):
        # Генерируем случайный email для каждого запуска
        random_part = "".join(
            random.choices(string.ascii_lowercase + string.digits, k=8)
        )
        return f"testuser_{random_part}@example.com"

    def test_successful_registration_and_avatar_display(self, browser):
        browser.get("https://qa-desk.stand.praktikum-services.ru/")

        # Нажать кнопку "Вход и регистрация"
        login_register_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and text()='Вход и регистрация']",
                )
            )
        )
        login_register_btn.click()

        # Нажать кнопку "Нет аккаунта"
        no_account_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and text()='Нет аккаунта']",
                )
            )
        )
        no_account_btn.click()

        # Заполнить email с уникальным значением
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        email = self.generate_random_email()
        email_input.clear()
        email_input.send_keys(email)

        # Ввести пароль и подтверждение
        password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.clear()
        password_input.send_keys("Qwerty123!")

        repeat_password_input = browser.find_element(
            By.CSS_SELECTOR, "input[name='submitPassword']"
        )
        repeat_password_input.clear()
        repeat_password_input.send_keys("Qwerty123!")

        # Нажать кнопку "Создать аккаунт"
        create_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonPrimary') and text()='Создать аккаунт']",
                )
            )
        )
        create_btn.click()

        # Ожидание перехода или появления аватара
        avatar_button = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.circleSmall"))
        )
        assert (
            avatar_button.is_displayed()
        ), "Аватар пользователя не отображается после регистрации"

        # Проверка отображения имени пользователя "User"
        user_name_elem = WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.profileText.name"))
        )
        assert (
            user_name_elem.is_displayed()
        ), "Имя пользователя не отображается после регистрации"
        assert (
            user_name_elem.text.strip() == "User."
        ), f"Ожидалось имя 'User.', но получено '{user_name_elem.text.strip()}'"

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestPasswordFieldsValidation:
    def test_password_fields_highlighted_red(self, browser):
        browser.get("https://qa-desk.stand.praktikum-services.ru/")

        login_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and contains(., 'Вход и регистрация')]",
                )
            )
        )
        login_btn.click()

        no_account_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and contains(., 'Нет аккаунта')]",
                )
            )
        )
        no_account_btn.click()

        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        email_input.clear()
        email_input.send_keys("йцвцйв")  # Некорректный email

        create_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonPrimary') and contains(., 'Создать аккаунт')]",
                )
            )
        )
        create_btn.click()

        def assert_color_is_red(element, css_property="border-color"):
            color = element.value_of_css_property(css_property)
            expected_colors = ["rgb(255, 105, 114)", "rgba(255, 105, 114, 1)"]
            assert (
                color in expected_colors
            ), f"Ожидался цвет {expected_colors}, но получен {color}"

        # Проверка Email
        email_field = browser.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_container = email_field.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'input_inputError__fLUP9')]"
        )
        assert "input_inputError__fLUP9" in email_container.get_attribute("class")
        assert_color_is_red(email_container, "border-color")

        error_message_element = email_field.find_element(
            By.XPATH,
            "./ancestor::div[3]/span[contains(@class, 'input_span__yWPqB') and text()='Ошибка']",
        )
        assert error_message_element.is_displayed()

        # Проверка Пароля
        password_field = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_container = password_field.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'input_inputError__fLUP9')]"
        )
        assert "input_inputError__fLUP9" in password_container.get_attribute("class")
        assert_color_is_red(password_container, "border-color")

        # Проверка Повторите пароль
        repeat_password_field = browser.find_element(
            By.CSS_SELECTOR, "input[name='submitPassword']"
        )
        repeat_password_container = repeat_password_field.find_element(
            By.XPATH, "./ancestor::div[contains(@class, 'input_inputError__fLUP9')]"
        )
        assert "input_inputError__fLUP9" in repeat_password_container.get_attribute(
            "class"
        )
        assert_color_is_red(repeat_password_container, "border-color")

        print(
            "\nВсе поля выделены цветом #FF6972, сообщение 'Ошибка' отображается под Email"
        )

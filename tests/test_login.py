from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestLogin:
    def test_login_and_check_avatar_and_username(self, browser):
        # Открываем страницу
        browser.get("https://qa-desk.stand.praktikum-services.ru")

        # Нажимаем кнопку "Вход и регистрация"
        login_register_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and text()='Вход и регистрация']",
                )
            )
        )
        login_register_btn.click()

        # Вводим логин (Email)
        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        email_input.clear()
        email_input.send_keys("manya.nzenliv123@gmail.com")

        # Вводим пароль
        password_input = browser.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.clear()
        password_input.send_keys("qwe123qwe")

        # Нажимаем кнопку "Войти"
        login_btn = browser.find_element(
            By.XPATH, "//button[contains(@class, 'buttonPrimary') and text()='Войти']"
        )
        login_btn.click()

        # Проверяем, что после входа отображается аватар пользователя (кнопка с классом circleSmall и svg внутри)
        avatar_button = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.circleSmall"))
        )
        assert avatar_button.is_displayed(), "Аватар пользователя не отображается"

        # Проверяем, что отображается имя пользователя "User"
        user_name_elem = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3.profileText.name"))
        )
        assert user_name_elem.is_displayed(), "Имя пользователя не отображается"
        assert (
            user_name_elem.text.strip() == "User."
        ), f"Ожидалось имя 'User.', но получено '{user_name_elem.text.strip()}'"

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestPlaceAdModal:
    def test_modal_shown_on_place_ad_click(self, browser):
        # Открываем главную страницу
        browser.get("https://qa-desk.stand.praktikum-services.ru/")

        # Нажимаем кнопку "Разместить объявление"
        place_ad_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonPrimary') and text()='Разместить объявление']",
                )
            )
        )
        place_ad_button.click()

        # Ожидаем появления модального окна с заголовком
        modal_title = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (
                    By.XPATH,
                    "//form[contains(@class, 'popUp_shell__LuyqR')]//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]",
                )
            )
        )
        assert modal_title.is_displayed(), "Модальное окно с заголовком не отображается"
        assert (
            modal_title.text.strip() == "Чтобы разместить объявление, авторизуйтесь"
        ), f"Ожидался заголовок 'Чтобы разместить объявление, авторизуйтесь', но получен '{modal_title.text.strip()}'"

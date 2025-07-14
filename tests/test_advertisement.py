from data.urls import Urls
from data.data import EXPECTED_MODAL_TITLE
from locators.locators import MainPageLocators, AuthLocators
from helpers.helpers import click_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestPlaceAdModal:
    def test_modal_shown_on_place_ad_click(self, browser):
        # Открываем главную страницу
        browser.get(Urls.MAIN_PAGE)

        # Нажимаем кнопку "Разместить объявление"
        click_element(browser, MainPageLocators.POST_AD_BUTTON)

        # Ожидаем появления модального окна с заголовком
        modal_title = WebDriverWait(browser, 50).until(
            EC.visibility_of_element_located(AuthLocators.MODAL_TITLE)
        )

        # Проверяем, что модальное окно отображается и заголовок корректен
        assert modal_title.is_displayed(), "Модальное окно с заголовком не отображается"
        assert modal_title.text.strip() == EXPECTED_MODAL_TITLE, (
            f"Ожидался заголовок '{EXPECTED_MODAL_TITLE}', "
            f"но получен '{modal_title.text.strip()}'"
        )

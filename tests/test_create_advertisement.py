import pytest
from data.urls import Urls
from data.data import (
    USER_EMAIL,
    USER_PASSWORD,
    LISTING_NAME,
    LISTING_DESCRIPTION,
    LISTING_PRICE,
    EXPECTED_CATEGORY,
    EXPECTED_CITY,
)
from locators.locators import AuthLocators, MainPageLocators, AdvertisementLocators
from helpers.helpers import click_element, fill_input, safe_click_avatar
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestCreateListing:
    def test_create_listing_and_check_in_profile(self, browser):
        # Открываем главную страницу
        browser.get(Urls.MAIN_PAGE)

        # Вход и регистрация
        click_element(browser, AuthLocators.LOGIN_REGISTER_BUTTON)
        fill_input(browser, AuthLocators.EMAIL_INPUT, USER_EMAIL)
        fill_input(browser, AuthLocators.PASSWORD_INPUT, USER_PASSWORD)
        click_element(browser, AuthLocators.LOGIN_BUTTON)

        # Ждем появления аватара после логина
        WebDriverWait(browser, 15).until(
            EC.visibility_of_element_located(AuthLocators.USER_AVATAR)
        )

        # Нажимаем "Разместить объявление"
        click_element(browser, MainPageLocators.POST_AD_BUTTON)

        # Заполнение формы объявления
        fill_input(browser, AdvertisementLocators.NAME_INPUT, LISTING_NAME)
        fill_input(
            browser, AdvertisementLocators.DESCRIPTION_TEXTAREA, LISTING_DESCRIPTION
        )
        fill_input(browser, AdvertisementLocators.PRICE_INPUT, LISTING_PRICE)

        # Проверяем выбранную категорию
        category_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AdvertisementLocators.CATEGORY_INPUT)
        )
        category_value = category_input.get_attribute("value")
        assert (
            category_value == EXPECTED_CATEGORY
        ), f"Ожидалось значение категории '{EXPECTED_CATEGORY}', но получено '{category_value}'"

        # Проверяем выбранный город
        city_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AdvertisementLocators.CITY_INPUT)
        )
        city_value = city_input.get_attribute("value")
        assert (
            city_value == EXPECTED_CITY
        ), f"Ожидалось значение города '{EXPECTED_CITY}', но получено '{city_value}'"

        # Проверяем, что кнопка "Опубликовать" активна
        publish_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(AdvertisementLocators.PUBLISH_BUTTON)
        )
        disabled = publish_btn.get_attribute("disabled")
        assert disabled is None, "Кнопка 'Опубликовать' заблокирована"

        # Скроллим к кнопке и кликаем разными способами для надежности
        browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", publish_btn
        )

        clicked = False
        for method in [
            publish_btn.click,
            lambda: browser.execute_script("arguments[0].click();", publish_btn),
            lambda: ActionChains(browser)
            .move_to_element(publish_btn)
            .click()
            .perform(),
            lambda: browser.execute_script(
                "arguments[0].submit();",
                publish_btn.find_element(By.XPATH, "./ancestor::form"),
            ),
        ]:
            try:
                method()
                clicked = True
                break
            except Exception:
                continue

        assert clicked, "Не удалось нажать кнопку 'Опубликовать' любым способом"

        # Переход в профиль пользователя — кликаем по аватару с защитой от stale element
        safe_click_avatar(browser, AuthLocators.USER_AVATAR)

        # Проверяем, что в блоке "Мои объявления" есть объявления
        my_ads_section = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(AdvertisementLocators.MY_ADS_SECTION)
        )
        ads = my_ads_section.find_elements(By.CSS_SELECTOR, "div.card")
        assert len(ads) > 0, "В блоке 'Мои объявления' нет объявлений"

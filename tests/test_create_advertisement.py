from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestCreateListing:
    def test_create_listing_and_check_in_profile(self, browser):
        listing_name = "Тестовое объявление"

        browser.get("https://qa-desk.stand.praktikum-services.ru/")

        # Вход и регистрация
        login_register_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonSecondary') and normalize-space(text())='Вход и регистрация']",
                )
            )
        )
        login_register_btn.click()

        email_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        email_input.clear()
        email_input.send_keys("manya.nzenliv123@gmail.com")

        password_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[name='password']")
            )
        )
        password_input.clear()
        password_input.send_keys("qwe123qwe")

        login_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonPrimary') and normalize-space(text())='Войти']",
                )
            )
        )
        login_btn.click()

        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.circleSmall"))
        )

        place_ad_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[contains(@class, 'buttonPrimary') and normalize-space(text())='Разместить объявление']",
                )
            )
        )
        place_ad_btn.click()

        # Заполнение формы
        name_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='name']"))
        )
        name_input.clear()
        name_input.send_keys(listing_name)

        description_textarea = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "textarea[name='description']")
            )
        )
        description_textarea.clear()
        description_textarea.send_keys("Описание тестового товара для автотеста.")

        price_input = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='price']"))
        )
        price_input.clear()
        price_input.send_keys("1500")

        # Выбор категории
        category_dropdown = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='category']"))
        )
        category_dropdown.click()

        category_option = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//div[contains(@class, 'dropDownMenu_hidden__qBq1t')]//button[.//span[text()='Авто']]",
                )
            )
        )
        category_option.click()

        # Выбор города
        city_dropdown_button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "button.dropDownMenu_arrowDown__pfGL1")
            )
        )
        city_dropdown_button.click()

        city_option = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button/span[text()='Москва']"))
        )
        city_option.click()

        # Выбор состояния товара
        condition_radio = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//input[@name='condition' and @value='Новый']")
            )
        )
        ActionChains(browser).move_to_element(condition_radio).click().perform()

        # Надежное нажатие кнопки "Опубликовать"
        publish_btn = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//button[@type='submit' and contains(@class, 'buttonPrimary') and normalize-space(text())='Опубликовать']",
                )
            )
        )

        # Проверяем, что кнопка не disabled
        disabled = publish_btn.get_attribute("disabled")
        assert disabled is None, "Кнопка 'Опубликовать' заблокирована"

        # Скроллим к кнопке
        browser.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", publish_btn
        )

        # Ждем, пока кнопка станет кликабельной (иногда нужно чуть больше времени)
        WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[@type='submit' and contains(@class, 'buttonPrimary') and normalize-space(text())='Опубликовать']",
                )
            )
        )

        clicked = False
        # 1. Пробуем обычный клик
        try:
            publish_btn.click()
            clicked = True
        except Exception:
            pass

        # 2. Клик через JS, если обычный не сработал
        if not clicked:
            try:
                browser.execute_script("arguments[0].click();", publish_btn)
                clicked = True
            except Exception:
                pass

        # 3. Клик через ActionChains, если предыдущие не сработали
        if not clicked:
            try:
                ActionChains(browser).move_to_element(publish_btn).click().perform()
                clicked = True
            except Exception:
                pass

        # 4. Отправка формы через JS, если кнопка в форме
        if not clicked:
            try:
                form = publish_btn.find_element(By.XPATH, "./ancestor::form")
                browser.execute_script("arguments[0].submit();", form)
                clicked = True
            except Exception:
                pass

        assert clicked, "Не удалось нажать кнопку 'Опубликовать' любым способом"

        # Переход в профиль пользователя
        user_avatar_btn = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.circleSmall"))
        )
        user_avatar_btn.click()

        # Проверяем появление объявления
        my_ads_section = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//section[contains(., 'Мои объявления')]")
            )
        )

        created_ad = my_ads_section.find_elements(
            By.XPATH, f".//div[contains(text(), '{listing_name}')]"
        )
        assert (
            len(created_ad) > 0
        ), "Созданное объявление не найдено в блоке 'Мои объявления'"

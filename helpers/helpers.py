from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import string
from selenium.common.exceptions import StaleElementReferenceException


def click_element(browser, locator, timeout=10):
    element = WebDriverWait(browser, timeout).until(EC.element_to_be_clickable(locator))
    element.click()


def fill_input(browser, locator, text, timeout=10):
    input_field = WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    input_field.clear()
    input_field.send_keys(text)


def assert_field_highlighted_red(
    browser, input_locator, error_container_locator, timeout=10
):
    """
    Проверяет, что поле подсвечено красным:
    - контейнер ошибки виден и содержит нужный класс
    - цвет рамки красный
    """
    try:
        container = WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located(error_container_locator)
        )
    except TimeoutException:
        assert (
            False
        ), f"Контейнер ошибки для поля {input_locator} не найден или не виден"

    classes = container.get_attribute("class")
    assert (
        "input_inputError__fLUP9" in classes
    ), f"Поле {input_locator} не содержит класс ошибки"

    color = container.value_of_css_property("border-color")
    expected_colors = ["rgb(255, 105, 114)", "rgba(255, 105, 114, 1)"]
    assert (
        color in expected_colors
    ), f"Ожидался цвет {expected_colors}, получен {color} для поля {input_locator}"


def assert_error_message_displayed(browser, error_message_locator, timeout=10):
    error_message = WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(error_message_locator)
    )
    assert error_message.is_displayed(), "Сообщение об ошибке не отображается"


def generate_random_email():
    """Генерирует валидный случайный email для регистрации."""
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    domain = "example.com"
    return f"{username}@{domain}"


def wait_for_element(browser, locator, timeout=10):
    return WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )


def wait_for_element_invisibility(browser, locator, timeout=10):
    WebDriverWait(browser, timeout).until(EC.invisibility_of_element_located(locator))


def assert_element_has_class(browser, locator, class_name, timeout=10):
    element = WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    classes = element.get_attribute("class")
    assert class_name in classes, f"Элемент {locator} не содержит класс '{class_name}'"


def assert_element_displayed(browser, locator, timeout=10):
    element = WebDriverWait(browser, timeout).until(
        EC.visibility_of_element_located(locator)
    )
    assert element.is_displayed(), f"Элемент {locator} не отображается"


def safe_click_avatar(browser, locator, retries=3, timeout=10):
    for _ in range(retries):
        try:
            element = WebDriverWait(browser, timeout).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
            return
        except StaleElementReferenceException:
            pass
    raise Exception(
        "Не удалось кликнуть по аватару пользователя из-за StaleElementReferenceException"
    )

from selenium.webdriver.common.by import By


class AuthLocators:
    """Локаторы для страницы авторизации"""

    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(., 'Вход и регистрация')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Пароль']")
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[contains(., 'Войти')]",
    )
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Выйти')]")
    MODAL_TITLE = (
        By.XPATH,
        "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]",
    )


class RegistrationLocators:
    LOGIN_REGISTER_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'buttonSecondary') and contains(., 'Вход и регистрация')]",
    )
    NO_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'buttonSecondary') and contains(., 'Нет аккаунта')]",
    )
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")
    CREATE_ACCOUNT_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'buttonPrimary') and contains(., 'Создать аккаунт')]",
    )
    AVATAR_BUTTON = (By.CSS_SELECTOR, "button.circleSmall")
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")
    EMAIL_ERROR_MESSAGE = (
        By.XPATH,
        "//input[@name='email']/ancestor::div[contains(@class, 'input_inputError__fLUP9')]/ancestor::div[1]/following-sibling::span[contains(@class, 'input_span__yWPqB') and contains(text(), 'Ошибка')]",
    )

    REPEAT_PASSWORD_ERROR_CONTAINER = (
        By.XPATH,
        "//input[@name='submitPassword']/ancestor::div[contains(@class, 'input_inputError__fLUP9')]",
    )

    PASSWORD_ERROR_CONTAINER = (
        By.XPATH,
        "//input[@name='password']/ancestor::div[contains(@class, 'input_inputError__fLUP9')]",
    )
    EMAIL_ERROR_CONTAINER = (
        By.XPATH,
        "//input[@name='email']/ancestor::div[contains(@class, 'input_inputError__fLUP9')]",
    )


class MainPageLocators:
    """Локаторы главной страницы"""

    POST_AD_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'buttonPrimary') and text()='Разместить объявление']",
    )
    AUTH_MODAL = (By.CSS_SELECTOR, ".auth-modal")
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")


class AdvertisementLocators:
    NAME_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    DESCRIPTION_TEXTAREA = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "input[name='category']")
    CATEGORY_OPTION_AUTO = (By.XPATH, "//button[.//span[text()='Авто']]")
    CITY_DROPDOWN_BUTTON = (By.CSS_SELECTOR, "button.dropDownMenu_arrowDown__pfGL1")
    CITY_OPTION_MOSCOW = (By.XPATH, "//button[.//span[text()='Москва']]")
    CONDITION_RADIO_NEW = (By.XPATH, "//input[@name='condition' and @value='Новый']")
    PUBLISH_BUTTON = (
        By.XPATH,
        "//button[@type='submit' and contains(@class, 'buttonPrimary') and normalize-space(text())='Опубликовать']",
    )
    MY_ADS_SECTION = (
        By.XPATH,
        "//h1[contains(text(), 'Мои объявления')]/following-sibling::div[contains(@class, 'profilePage_gridAndPaginaton__togPs')]",
    )
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")
    CATEGORY_INPUT = (By.CSS_SELECTOR, "input[name='category']")
    CITY_INPUT = (By.CSS_SELECTOR, "input[name='city']")


class MainPageLocators:
    POST_AD_BUTTON = (
        By.XPATH,
        "//button[contains(@class, 'buttonPrimary') and contains(., 'Разместить объявление')]",
    )
    AUTH_MODAL = (By.CSS_SELECTOR, ".auth-modal")
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")

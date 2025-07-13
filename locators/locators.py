from selenium.webdriver.common.by import By


class AuthLocators:
    # Кнопки
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(., 'Вход и регистрация')]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Войти')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(., 'Выйти')]")

    # Поля формы
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='Введите Email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[placeholder='Пароль']")

    # Элементы после входа (на основе вашего HTML)
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")  # Кнопка с аватаром
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")  # Имя пользователя

    # Кнопка размещения объявления
    POST_AD_BUTTON = (By.XPATH, "//button[contains(., 'Разместить объявление')]")


class RegistrationLocators:
    # Кнопки
    LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(., 'Вход и регистрация')]")
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")

    # Поля формы
    REG_EMAIL_INPUT = (By.CSS_SELECTOR, "input[name='email']")
    REG_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='password']")
    REG_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, "input[name='submitPassword']")

    # Элементы профиля (после регистрации)
    USER_PROFILE_SECTION = (By.CSS_SELECTOR, "div.flexRow")  # Основной контейнер
    USER_AVATAR = (By.CSS_SELECTOR, "button.circleSmall")  # Кнопка аватара
    USER_NAME = (By.CSS_SELECTOR, "h3.profileText.name")  # Имя пользователя (с точкой)
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.btnSmall")  # Кнопка выхода
    PLACE_AD_BUTTON = (By.XPATH, "//button[contains(., 'Разместить объявление')]")


class MainPageLocators:
    POST_AD_BUTTON = (By.CSS_SELECTOR, ".post-ad-button")
    AUTH_MODAL = (By.CSS_SELECTOR, ".auth-modal")
    MODAL_TITLE = (By.CSS_SELECTOR, ".modal-title")


class AdvertisementLocators:
    TITLE_INPUT = (By.CSS_SELECTOR, "input[name='name']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_INPUT = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_DROPDOWN = (By.CSS_SELECTOR, "div.dropDownMenu_hidden__qBq1t button")
    CITY_DROPDOWN = (By.CSS_SELECTOR, "div.dropDownMenu_hidden__qBq1t button")
    CONDITION_RADIO = (By.XPATH, "//input[@name='condition' and @value='Б/У']")
    PUBLISH_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'buttonPrimary') and text()='Опубликовать']")
    MY_ADS_SECTION = (By.XPATH, "//section[contains(., 'Мои объявления')]")
    CONDITION_RADIO_NEW = (By.XPATH, "//input[@name='condition' and @value='Новый']")
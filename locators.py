from selenium.webdriver.common.by import By

class Locators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/parent::div/input")
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/parent::div/input")
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/parent::div/input")

    REGISTER_BUTTON = (By.XPATH, "//main//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']")

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")

    LOGIN_BUTTON_MANE_PAGE = (By.XPATH, "//button[text()='Войти в аккаунт']")
    LOGIN_BUTTON_REG_PAGE = (By.XPATH, "//p[text()='Уже зарегистрированы?']/a")
    LOGIN_BUTTON_FORGOT_PAGE = (By.XPATH, "//p[text()='Вспомнили пароль?']/a")

    PROFILE_BUTTON = (By.XPATH, "//a[text()='Профиль']")

    DESIGNER_BUTTON = (By.XPATH, "//p[text()='Конструктор']/parent::a")

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

    BUN_BUTTON = (By.XPATH, "//span[text()='Булки']")
    SAUCES_BUTTON = (By.XPATH, "//span[text()='Соусы']")
    TOPPINGS_BUTTON = (By.XPATH, "//span[text()='Начинки']")

    ACTIVE_BUN_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']")
    ACTIVE_SOUCES_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']")
    ACTIVE_TOPPINGS_BUTTON = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Начинки']")

    LOGIN_TITLE = (By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")
    MANE_PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

    TOPPINGS_TITLE = (By.XPATH, "//h2[text()='Начинки']")
    
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error.text_type_main-default")

    LOGO = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import MAIN_URL, LOGIN_URL, REGISTER_URL, FORGOT_PASSWORD_URL

class TestEntry:

    def test_button_login_your_account_in_main_page(self, driver):
        driver.get(MAIN_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TITLE))

        assert LOGIN_URL == driver.current_url


    def test_button_personal_account_in_main_page(self, driver):
        driver.get(MAIN_URL)

        driver.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TITLE))

        assert LOGIN_URL == driver.current_url


    def test_login_button_in_registration_page(self, driver):
        driver.get(REGISTER_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_REG_PAGE).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TITLE))

        assert LOGIN_URL == driver.current_url


    def test_login_button_in_forgot_password_page(self, driver):
        driver.get(FORGOT_PASSWORD_URL)

        driver.find_element(*Locators.LOGIN_BUTTON_FORGOT_PAGE).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TITLE))

        assert LOGIN_URL == driver.current_url

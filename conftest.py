import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import LOGIN_URL, LOGIN_MAIL, LOGIN_PASSWORD
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture
def driver_log(driver):
    driver.get(LOGIN_URL)
    
    driver.find_element(*Locators.EMAIL_INPUT).send_keys(LOGIN_MAIL)
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys(LOGIN_PASSWORD)
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))

    return driver
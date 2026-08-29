import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from constants import LOGIN_URL
from locators import Locators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture
def driver_log(driver):
    driver.get(LOGIN_URL)
    
    driver.find_element(*Locators.EMAIL_INPUT).send_keys("дмитрий_варавва_53_000@mail.ru")
    driver.find_element(*Locators.PASSWORD_INPUT).send_keys("76543210")
    driver.find_element(*Locators.LOGIN_BUTTON).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))

    return driver
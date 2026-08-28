from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import MAIN_URL

class TestBurgerConstructor:

    def test_transition_to_bun(self, driver):
        driver.get(MAIN_URL)

        #прокрутка вниз чтобы кнопка Булки перестала быть активной
        element = driver.find_element(*Locators.TOPPINGS_TITLE)
        driver.execute_script("arguments[0].scrollIntoView();", element)

        #ожидание переключения активности кнопки с Булки на Начинки
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ACTIVE_TOPPINGS_BUTTON))

        driver.find_element(*Locators.BUN_BUTTON).click()

        assert WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ACTIVE_BUN_BUTTON))


    def test_transition_to_sauces(self, driver):
        driver.get(MAIN_URL)

        driver.find_element(*Locators.SAUCES_BUTTON).click()

        assert WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ACTIVE_SOUCES_BUTTON))


    def test_transition_to_toppings(self, driver):
        driver.get(MAIN_URL)

        driver.find_element(*Locators.TOPPINGS_BUTTON).click()

        assert WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.ACTIVE_TOPPINGS_BUTTON))

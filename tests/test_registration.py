from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import REGISTER_URL
import random

class TestRegistration:

    def test_succes_registration(self, driver):
        driver.get(REGISTER_URL)

        email = f'дмитрий_варавва_53_{random.randint(100, 999)}@mail.ru'

        #заполнение полей
        driver.find_element(*Locators.NAME_INPUT).send_keys("Адам")
        driver.find_element(*Locators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Locators.PASSWORD_INPUT).send_keys("76543210")

        #клик по кнопке регистрации
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        #ожидание загрузки элемента на новой странице
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TITLE))


    def test_incorrect_password_get_error_message(self, driver):
        driver.get(REGISTER_URL)

        password = str(random.randint(0, 99999))

        driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)

        #клик по кнопке чтобы снять фокус с поля
        driver.find_element(*Locators.REGISTER_BUTTON).click()

        #ожидание и поиск сообщения об ошибке
        assert WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.ERROR_MESSAGE))
        
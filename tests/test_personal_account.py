from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from constants import MAIN_URL, PROFILE_URL, LOGIN_URL

class TestPersonalAccount:

    def test_go_to_lk_from_main_page_via_pesonal_account_button(self, driver_log):

        #клик по кнопке Личный кабинет
        driver_log.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        #ожидание загрузки страницы
        WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))

        #проверка открыта ли нужная страница
        assert PROFILE_URL == driver_log.current_url


    def test_go_to_main_page_from_lk_with_click_designer_button(self, driver_log):
        
        driver_log.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        #ожидание загрузки страницы
        WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))

        driver_log.find_element(*Locators.DESIGNER_BUTTON).click()

        WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))

        assert MAIN_URL == driver_log.current_url


    def test_go_to_main_page_from_lk_with_click_on_logo(self, driver_log):

        driver_log.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))
        
        driver_log.find_element(*Locators.LOGO).click()

        WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located(Locators.MAIN_PAGE_TITLE))

        assert MAIN_URL == driver_log.current_url


    def test_logout_in_lk(self, driver_log):

        driver_log.find_element(*Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located(Locators.PROFILE_BUTTON))

        driver_log.find_element(*Locators.LOGOUT_BUTTON).click()

        WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located(Locators.LOGIN_TITLE))

        assert LOGIN_URL == driver_log.current_url

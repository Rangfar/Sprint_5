from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_go_to_lk_from_main_page_via_pesonal_account_button(driver):

    #клик по кнопке Личный кабинет
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']/parent::a").click()
    #ожидание загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))

    required_url = "https://stellarburgers.education-services.ru/account/profile"

    #проверка открыта ли нужная страница
    assert required_url == driver.current_url

    driver.close()

def test_go_to_main_page_from_lk_with_click_designer_button(driver):
    #клик по кнопке Личный кабинет
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']/parent::a").click()
    #ожидание загрузки страницы
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))

    driver.find_element(By.XPATH, "//p[text()='Конструктор']/parent::a").click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

    required_url = "https://stellarburgers.education-services.ru/"
    assert required_url == driver.current_url

    driver.close()

def test_go_to_main_page_from_lk_with_click_on_logo(driver):
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']/parent::a").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))
    
    driver.find_element(By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']").click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
    
    required_url = "https://stellarburgers.education-services.ru/"
    assert required_url == driver.current_url
    driver.close()

def test_logout_in_lk(driver):
    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']/parent::a").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//a[text()='Профиль']")))

    driver.find_element(By.XPATH, "//button[text()='Выход']").click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

    required_url = "https://stellarburgers.education-services.ru/login"
    assert required_url == driver.current_url

    driver.close()

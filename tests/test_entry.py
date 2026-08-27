from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_button_login_your_account_in_main_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg").click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

    required_url = "https://stellarburgers.education-services.ru/login"
    assert required_url == driver.current_url

    driver.close()

def test_button_personal_account_in_main_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']/parent::a").click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

    required_url = "https://stellarburgers.education-services.ru/login"
    assert required_url == driver.current_url

    driver.close()

def test_login_button_in_registration_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")

    driver.find_element(By.XPATH, "//p[text()='Уже зарегистрированы?']/a").click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

    required_url = "https://stellarburgers.education-services.ru/login"
    assert required_url == driver.current_url

    driver.close()

def test_login_button_in_forgot_password_page():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/forgot-password")

    driver.find_element(By.XPATH, "//p[text()='Вспомнили пароль?']/a").click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

    required_url = "https://stellarburgers.education-services.ru/login"
    assert required_url == driver.current_url

    driver.close()
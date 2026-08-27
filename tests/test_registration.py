from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import random

def test_succes_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")

    email = f'дмитрий_варавва_53_{random.randint(100, 999)}@mail.ru'

    #заполнение полей
    driver.find_element(By.XPATH, "//label[text()='Имя']/parent::div/input").send_keys("Адам")
    driver.find_element(By.XPATH, "//label[text()='Email']/parent::div/input").send_keys(email)
    driver.find_element(By.XPATH, "//label[text()='Пароль']/parent::div/input").send_keys("76543210")

    #клик по кнопке регистрации
    driver.find_element(By.XPATH, "//main//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

    #ожидание загрузки элемента на новой странице
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='Auth_login__3hAey']/h2[text()='Вход']")))

    driver.close()

def test_incorrect_password_get_error_message():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")

    password = str(random.randint(0, 99999))

    driver.find_element(By.XPATH, "//label[text()='Пароль']/parent::div/input").send_keys(password)

    #клик по кнопке чтобы снять фокус с поля
    driver.find_element(By.XPATH, "//main//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']").click()

    #ожидание и поиск сообщения об ошибке
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".input__error.text_type_main-default")))
    text_error = driver.find_element(By.CSS_SELECTOR, ".input__error.text_type_main-default").text

    assert text_error == "Некорректный пароль"

    driver.close()
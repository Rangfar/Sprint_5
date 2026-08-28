import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.close()


@pytest.fixture
def driver_log():
    driver_log = webdriver.Chrome()
    driver_log.get("https://stellarburgers.education-services.ru/login")
    
    driver_log.find_element(By.XPATH, "//label[text()='Email']/parent::div/input").send_keys("дмитрий_варавва_53_000@mail.ru")
    driver_log.find_element(By.XPATH, "//label[text()='Пароль']/parent::div/input").send_keys("76543210")
    driver_log.find_element(By.XPATH, "//button[text()='Войти']").click()

    WebDriverWait(driver_log, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

    #строка кода ниже была добавлена благодаря подсказке нейросети, так как информации о ней нет в теории практикума
    yield driver_log

    driver_log.close()
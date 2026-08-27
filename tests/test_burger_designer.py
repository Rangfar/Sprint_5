from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_transition_to_bun():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    #прокрутка вниз чтобы кнопка Булки перестала быть активной
    element = driver.find_element(By.XPATH, "//h2[text()='Начинки']")
    driver.execute_script("arguments[0].scrollIntoView();", element)

    #ожидание переключения активности кнопки с Булки на Начинки
    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Начинки']")))

    driver.find_element(By.XPATH, "//span[text()='Булки']").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Булки']")))

    driver.close()

def test_transition_to_sauces():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(By.XPATH, "//span[text()='Соусы']").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Соусы']")))

    driver.close()

def test_transition_to_toppings():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/")

    driver.find_element(By.XPATH, "//span[text()='Начинки']").click()

    WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, "//div[contains(@class, 'tab_tab_type_current__2BEPc')]/span[text()='Начинки']")))

    driver.close()
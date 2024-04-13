import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)    # - globally for all of tests
    yield driver
    driver.quit()


def test_registration_functional(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    driver.find_element(By.XPATH, "//h1")
    driver.find_element(By.XPATH, "//*[@id='startTest']").click()
    driver.find_element(By.XPATH, "//input[@id='login']").send_keys('standard_user')
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys('secret_sauce')
    driver.find_element(By.XPATH, "//input[@id='agree']").click()
    driver.find_element(By.XPATH, "//*[@id='register']").click()
    driver.find_element(By.XPATH, "//*[@id='loader']")
    time.sleep(5)
    SUCCESS_MESSAGE = driver.find_element(By.XPATH, "//*[@id='successMessage']")
    assert SUCCESS_MESSAGE.text == "Вы успешно зарегистрированы!", "Text is not found"


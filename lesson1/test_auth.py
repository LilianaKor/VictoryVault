from selenium import webdriver 
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()

def test_auth_positive():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    assert browser.current_url == 'https://www.saucedemo.com/v1/inventory.html', 'url не соответствует ожидаемому'

    browser.quit()

def test_auth_negative():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('no_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()
    error_message = browser.find_element(By.XPATH, '//div[@class = "error-message-container error"]')
    assert error_message.is_displayed()
    print(error_message.text)


def login():
    browser.get('https://www.saucedemo.com/')
    browser.implicitly_wait(10)
    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()


def test_auth_transition_to_cart_by_name():
    login()
    item_title = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    item_title.click()


    browser.quit()



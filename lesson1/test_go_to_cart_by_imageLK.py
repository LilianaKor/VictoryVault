from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()

def test_transition_to_cart_by_foto():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    backpack_foto = browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img')
    backpack_foto.click()
    time.sleep(3)
    # Assertion to check if the URL contains the product ID
    assert 'inventory-item.html?id=4' in browser.current_url

    # Assertion to check if the correct product is displayed on the page
    backpack_title = browser.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name']").text
    assert backpack_title == 'Sauce Labs Backpack'


def test_transition_to_cart_by_name():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()

    # Click on the product name
    backpack_name = browser.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']")
    backpack_name.click()
    time.sleep(4)

    # Assertion to check if the correct product is displayed on the page
    product_title = browser.find_element(By.CSS_SELECTOR, "div[class='inventory_details_name']").text
    print(product_title)
    time.sleep(4)
    assert product_title == 'Sauce Labs Backpack'



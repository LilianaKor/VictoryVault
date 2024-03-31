from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()

def test_add_item_into_cartLKor():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    item_text_before = browser.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link']").text
    print(item_text_before)
    time.sleep(3)
    button = browser.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button.click()
    time.sleep(4)

    cart = browser.find_element(By.CSS_SELECTOR, "a[class = 'shopping_cart_link']")
    cart.click()

    item_text_after = browser.find_element(By.CSS_SELECTOR, "a[id = 'item_4_title_link']").text
    time.sleep(4)
    assert item_text_before == item_text_after

    browser.quit()
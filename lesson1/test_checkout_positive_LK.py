from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()

def test_checkout_positive():
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()

    # Clicking on product name to navigate to product card (assuming this step is required)
    product_name = browser.find_element(By.XPATH, "//div[@class='inventory_item_name' and text()='Sauce Labs Backpack']")
    product_name.click()
    time.sleep(2)

   # assert 'inventory-item.html?id=4' in browser.current_url
    add_to_cart_button = browser.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    add_to_cart_button.click()
    time.sleep(4)

    shopping_cart_link = browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    shopping_cart_link.click()
    time.sleep(3)
    assert 'cart.html' in browser.current_url

    checkout_button = browser.find_element(By.XPATH, "//a[text()='CHECKOUT']")
    checkout_button.click()
    time.sleep(4)

    # Fill in checkout information
    browser.find_element(By.ID, 'first-name').send_keys('Cece')
    browser.find_element(By.ID, 'last-name').send_keys('Mous')
    browser.find_element(By.ID, 'postal-code').send_keys('90401')

    # Click on continue to complete the checkout
    continue_button = browser.find_element(By.XPATH, "//input[@value='CONTINUE']")
    continue_button.click()
    time.sleep(3
               )

    # Assertion to check if the user is navigated to the next step of checkout (assuming there's a confirmation page)
    assert 'checkout-step-two.html' in browser.current_url



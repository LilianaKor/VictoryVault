from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
# After clicking on the checkout button
#WebDriverWait(browser, 10).until(EC.url_contains('checkout-step-two.html'))

def test_checkout_positive():
    browser = webdriver.Chrome()
    browser.get('https://www.saucedemo.com/v1/')

    browser.find_element(By.ID, 'user-name').send_keys('standard_user')
    browser.find_element(By.ID, 'password').send_keys('secret_sauce')
    browser.find_element(By.ID, 'login-button').click()

    # Clicking on product name to navigate to product card (assuming this step is required)
    product_name = browser.find_element(By.XPATH,"//*[@id='item_4_title_link']")
    product_name.click()
    #time.sleep(2)

   # assert 'inventory-item.html?id=4' in browser.current_url
    add_to_cart_button = browser.find_element(By.XPATH, "//button[text()='ADD TO CART']")
    add_to_cart_button.click()
    #time.sleep(4)

    shopping_cart_link = browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
    shopping_cart_link.click()
    #time.sleep(3)
    assert 'cart.html' in browser.current_url

    checkout_button = browser.find_element(By.XPATH, "//a[text()='CHECKOUT']")
    checkout_button.click()
    #time.sleep(4)

    # Fill in checkout information
    browser.find_element(By.ID, 'first-name').send_keys('Cece')
    browser.find_element(By.ID, 'last-name').send_keys('Mous')
    browser.find_element(By.ID, 'postal-code').send_keys('90401')

    # Click on continue to complete the checkout
    continue_button = browser.find_element(By.XPATH, "//input[@value='CONTINUE']")
    continue_button.click()
    #time.sleep(3)
    WebDriverWait(browser, 10).until(EC.url_contains('checkout-step-two.html'))

    # Assertion to check if the user is navigated to the next step of checkout (assuming there's a confirmation page)
    assert 'checkout-step-two.html' in browser.current_url

    browser.quit()

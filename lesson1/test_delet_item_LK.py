from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)

# def test_add_item_into_cartLKor():
#     browser.get('https://www.saucedemo.com/cart.html')
#     # browser.find_element(By.XPATH,"//div/button [@name = 'remove-sauce-labs-backpack']")
#     cart = browser.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
#     cart.click()

#     # Delete item from the cart
#     delete_button = browser.find_element(By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']")
#     delete_button.click()
#     time.sleep(3)

def test_add_item_into_cartLKor():
    browser.get('https://www.saucedemo.com/')

    browser.find_element('xpath', '//*[@id="user-name"]').send_keys('standard_user')
    browser.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    browser.find_element(By.XPATH, '//*[@id="login-button"]').click()

    item_text_before = browser.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link']").text
    #print(item_text_before)
    button = browser.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-backpack']")
    button.click()
   # time.sleep(2)

    cart = browser.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    cart.click()

    item_text_after = browser.find_element(By.CSS_SELECTOR, "a[id='item_4_title_link']").text
   # time.sleep(2)
    assert item_text_before == item_text_after

    shopping_cart_badge = browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']")
    assert shopping_cart_badge.is_displayed()
   # time.sleep(10)
    print(shopping_cart_badge)

#def test_delete_item_from_cartLKor():
    # Assuming the item has already been added to the cart  # Navigate to the cart page
    # cart = browser.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']")
    # time.sleep(3)
    # cart.click()
    #cart_badge_before = browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    # print(cart_badge_before)

 # # Delete item from the cart
   # basket = browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    basket = browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").text
    assert basket == '1'
    delete_button = browser.find_element(By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']")
    delete_button.click()
 #    time.sleep(5)

    cart_badge_after = browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").text
    print(cart_badge_after)
 #    time.sleep(2)
    assert cart_badge_after == ''
 #    time.sleep(3)

# Verify if the item is removed from the cart
# empty_cart_message = browser.find_element(By.CSS_SELECTOR, "div[class='cart_list']").text
#assert "Your cart is empty" in empty_cart_message .



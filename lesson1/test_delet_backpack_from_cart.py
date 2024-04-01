from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time

browser = webdriver.Chrome()
browser.implicitly_wait(5)

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
    time.sleep(5)
    print(shopping_cart_badge)

   # basket = browser.find_element(By.XPATH, "//span[@class='shopping_cart_badge']").text
    basket = browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").text
    assert basket == '1'
    delete_button = browser.find_element(By.CSS_SELECTOR, "button[data-test='remove-sauce-labs-backpack']")
    delete_button.click()
    time.sleep(3)

    cart_badge_after = browser.find_element(By.XPATH, "//a[@class='shopping_cart_link']").text
    print(cart_badge_after)
    time.sleep(4)
    assert cart_badge_after == ''
    time.sleep(2)


def test_remove_from_cart_from_item_card():
    browser.get("https://www.saucedemo.com/")

    username_field = browser.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = browser.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = browser.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    item_button = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    item_button.click()

    # adding item to the cart
    add_to_cart_button = browser.find_element(By.XPATH, '//button[@class ="btn btn_primary btn_small btn_inventory"]')
    add_to_cart_button.click()
    time.sleep(3)
    #
    # # removing item from the item card
    remove_button = browser.find_element(By.XPATH, '//button[@class="btn btn_secondary btn_small btn_inventory"]')
    remove_button.click()
    time.sleep(3)
    #
    # assert add_to_cart_button.is_displayed()
    assert "Remove" not in browser.page_source
    assert "Add to cart" in browser.page_source

    cart_button = browser.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a')
    cart_button.click()
    time.sleep(3)

    assert "Sauce Labs Backpack" not in browser.page_source

    browser.quit()


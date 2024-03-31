from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()


def test_item_image():
    browser.get("https://www.saucedemo.com/")

    username_field = browser.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = browser.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = browser.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()
    time.sleep(4)

    # clicking on the item image
    item_image = browser.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img')
    item_image.click()
    time.sleep(5)

    assert browser.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    assert "Sauce Labs Backpack" in browser.page_source

    browser.quit()

def test_transit_item_title():
    browser.get("https://www.saucedemo.com/")

    username_field = browser.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = browser.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = browser.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    # clicking on the item title
    item_title = browser.find_element(By.XPATH, '//*[@id="item_4_title_link"]/div')
    time.sleep(4)
    item_title.click()
    time.sleep(4)

    assert browser.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"
    assert "Sauce Labs Backpack" in browser.page_source
    browser.quit()

# Карточка товара
# Успешный переход к карточке товара после клика на картинку товара
# Успешный переход к карточке товара после клика на название товара

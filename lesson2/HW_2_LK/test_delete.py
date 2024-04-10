from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from selenium.common import exceptions
from lesson2.HW_2_LK.data import *
from lesson2.HW_2_LK.locators import *

#browser = webdriver.Chrome()

def test_auth_negative(driver):
    driver.get(MAIN_PAGE)
    driver.find_element('xpath', '//*[@id="user-name"]').send_keys('no_user')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('secret_sauce')
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    error_message = driver.find_element(By.XPATH, '//div[@class = "error-message-container error"]')
    assert error_message.is_displayed()
    print(error_message.text)


def test_add_item_to_cart_from_catalog(driver, login):
    driver.find_element(*BACKPACK_ADD_BUTTON).click()
    cart_button = driver.find_element(*CART_BUTTON).click()
    backpack_item = driver.find_element(*BACKPACK_ITEM)
    #assert backpack_item.is_displayed() is True
    assert backpack_item.text == 'Sauce Labs Backpack'


def test_delete_item(driver, login,):
    driver.find_element(*BACKPACK_ADD_BUTTON).click()
    cart_button = driver.find_element(*CART_BUTTON).click()
    backpack_item = driver.find_element(*BACKPACK_ITEM)
    driver.find_element(*REMOVE_BUTTON).click()


def test_remove_from_item_card(driver, login):
    driver.find_element(*BACKPACK_ITEM).click()
    driver.find_element(*ADD_SHOPCART_FROM_CART).click()
    assert driver.find_element(*BADGE).is_displayed()
    driver.find_element(*REMOVE_FROM_CART).click()


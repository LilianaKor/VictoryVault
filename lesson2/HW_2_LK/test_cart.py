from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from lesson2.HW_2_LK.data import *
from lesson2.HW_2_LK.locators import *

#browser = webdriver.Chrome()


def test_add_item_to_cart_from_catalog(driver, login):
    driver.find_element(*BACKPACK_ADD_BUTTON).click()
    #cart_button = driver.find_element(By.CLASS_NAME, 'shopping_cart_link')
    cart_button = driver.find_element(*CART_BUTTON)
    cart_button.click()
    backpack_item = driver.find_element(*BACKPACK_ITEM)
    #assert backpack_item.is_displayed() is True
    assert backpack_item.text == 'Sauce Labs Backpack'



    driver.quit()
from selenium.webdriver.common.by import By

USERNAME_FIELD = (By.XPATH, '//input[@data-test="username"]')
PASSWORD_FIELD = (By.XPATH, '//input[@data-test="password"]')
LOGIN_BUTTON = (By.XPATH, '//input[@data-test="login-button"]')
    # from cart
BACKPACK_ADD_BUTTON = (By.ID, 'add-to-cart-sauce-labs-backpack')
BACKPACK_ITEM = (By.XPATH, '//*[@id="item_4_title_link"]/div') # Title
REMOVE_FROM_CART = (By.XPATH, '//*[@data-test="remove"]')

CART_BUTTON = (By.CLASS_NAME, 'shopping_cart_link')
REMOVE_BUTTON = (By.CSS_SELECTOR, 'button[data-test="remove-sauce-labs-backpack"]')
ADD_TO_CART = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')

ADD_SHOPCART_FROM_CART = (By.CSS_SELECTOR, '#add-to-cart')
BADGE = (By.CSS_SELECTOR, '#shopping_cart_container > a > span')

FIND_BY_TEXT = '//*[text()="{}"]'
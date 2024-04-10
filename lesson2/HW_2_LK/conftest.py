import time
from selenium.webdriver.chrome.options import Options
from faker import Faker
import pytest
from selenium import webdriver
from lesson2.HW_2_LK.data import *
from lesson2.HW_2_LK.locators import *
from selenium.webdriver.common.by import By
from data import LOGIN, PASSWORD

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(*USERNAME_FIELD).send_keys(LOGIN)
    driver.find_element(*PASSWORD_FIELD).send_keys(PASSWORD)
    driver.find_element(*LOGIN_BUTTON).click()

# @pytest.fixture()
# def browser():
#     browser = webdriver.Chrome()
#     yield browser
#     print('\nquit browser...')
#     browser.quit()

# @pytest.fixture(scope='function', autouse=True)
# def browser(request):
#     print(f'\nStart test: {request.node.name}')
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new")
#     browser = webdriver.Chrome(options=chrome_options)
#     # browser = webdriver.Chrome()
#     browser.implicitly_wait(5)
#     yield browser
#     browser.quit()
#     print("\nEnd test")
#
#
# @pytest.fixture
# def fake_password():
#     fake = Faker()
#     return fake.password()
#
#
# @pytest.fixture
# def fake_username():
#     fake = Faker()
#     return fake.user_name()
#
#
# @pytest.fixture
# def fake_firstname():
#     fake = Faker()
#     return fake.first_name()
#
#
# @pytest.fixture
# def fake_lastname():
#     fake = Faker()
#     return fake.last_name()
#
#
# @pytest.fixture
# def fake_zipcode():
#     fake = Faker()
#     return fake.zipcode()


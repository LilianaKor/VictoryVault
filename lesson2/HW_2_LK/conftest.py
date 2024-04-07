import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from faker import Faker


@pytest.fixture(scope='function', autouse=True)
def browser(request):
    print(f'\nStart test: {request.node.name}')
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    browser = webdriver.Chrome(options=chrome_options)
    # browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
    print("\nEnd test")


@pytest.fixture
def fake_password():
    fake = Faker()
    return fake.password()


@pytest.fixture
def fake_username():
    fake = Faker()
    return fake.user_name()


@pytest.fixture
def fake_firstname():
    fake = Faker()
    return fake.first_name()


@pytest.fixture
def fake_lastname():
    fake = Faker()
    return fake.last_name()


@pytest.fixture
def fake_zipcode():
    fake = Faker()
    return fake.zipcode()










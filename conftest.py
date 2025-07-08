import pytest
import requests
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from page_object.recover_page import RecoverPage
from page_object.profile_page import ProfilePage
from page_object.order_feed_page import OrderFeedPage
from page_object.main_page import MainPage
from page_object.login_page import LoginPage
from helpers import generation_mail
from data import ingredient_names

@pytest.fixture(params=['Chrome', 'Firefox'])
def driver(request):
    if request.param == 'Chrome':
        browser_name = 'Chrome'
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
    else:
        browser_name = 'Firefox'
        options = FirefoxOptions()
        options.add_argument('--width=1920')
        options.add_argument('--height=1080')
        driver = webdriver.Firefox(options=options)

    yield driver
    driver.quit()

@pytest.fixture
def recover_page(driver):
    page = RecoverPage(driver)
    return page

@pytest.fixture
def profile_page(driver):
    page = ProfilePage(driver)
    return page

@pytest.fixture
def order_feed_page(driver):
    page = OrderFeedPage(driver)
    return page

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    return page

@pytest.fixture
def create_user():
    user_data = {
        "name": "volkov_user",
        "email": f"{generation_mail()}",
        "password": "Test123!"

    }

    response = requests.post(
        url = "https://stellarburgers.nomoreparties.site/api/auth/register",
        json = user_data
    )
    yield response, user_data
    refresh_token = response.json()["refreshToken"]
    token = response.json()["accessToken"]
    requests.delete(
        url="https://stellarburgers.nomoreparties.site/api/auth/user",
        data=refresh_token,
        headers={'Authorization': token}
    )

@pytest.fixture
def authorized_user(create_user, login_page):
    _, user_data = create_user
    login_page.auto_user(user_data['email'], user_data['password'])
    return user_data


@pytest.fixture
def create_order(create_user):
    response, _ = create_user
    token = response.json()["accessToken"]
    params = {"ingredients": random.choice(ingredient_names)}
    response = requests.post( url = "https://stellarburgers.nomoreparties.site/api/orders",
                             json=params,
                             headers={'Authorization': token})
    return response


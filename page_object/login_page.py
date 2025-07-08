from page_object.base_page import BasePage
import allure
from locators.login_page_locators import LoginPageLocators
from data import URL_LOGIN, user_data_for_login


class LoginPage(BasePage):

    @allure.step('Авторизация пользователя')
    def auto_user(self, email, password):
        self.go_to_url(URL_LOGIN)
        self.add_text_to_element(LoginPageLocators.INPUT_FIELD_EMAIL, email)
        self.add_text_to_element(LoginPageLocators.INPUT_FIELD_PASS, password)
        self.click_to_element(LoginPageLocators.BUTTON_LOGIN)





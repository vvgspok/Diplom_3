from data import URL_LOGIN
from page_object.base_page import BasePage
import allure
from locators.login_page_locators import LoginPageLocators
from locators.recover_page_locators import RecoverPageLocators
from helpers import generation_mail, generate_random_string


class RecoverPage(BasePage):

    @allure.step('Переход на страницу восстановления пароля')
    def go_to_page_password_recovery(self):
        self.go_to_url(URL_LOGIN)
        self.click_to_element(LoginPageLocators.BUTTON_RECOVER_PASSWORD)

    @allure.step('Отправка письма для восстановления')
    def submit_recovery_email(self):
        self.find_element_with_wait(RecoverPageLocators.RECOVER_FORM_NAME)
        self.add_text_to_element(RecoverPageLocators.INPUT_FIELD_EMAIL, generation_mail())
        self.click_to_element(RecoverPageLocators.BUTTON_RECOVER)

    @allure.step('Заполнить поле пароль и код')
    def fill_password_and_code_field(self):
        self.add_text_to_element(RecoverPageLocators.INPUT_FIELD_PASSWORD, generate_random_string())
        self.add_text_to_element(RecoverPageLocators.INPUT_FIELD_CODE, generate_random_string())


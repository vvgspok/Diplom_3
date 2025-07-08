from locators.profile_page_locators import ProfilePageLocators
from page_object.base_page import BasePage
import allure
from locators.login_page_locators import LoginPageLocators


class ProfilePage(BasePage):

    @allure.step('Переход на страницу история заказов пользователя')
    def click_go_to_order_history(self):
        self.click_to_element(ProfilePageLocators.BUTTON_SECTION_ORDER_HISTORY)
        self.find_element_with_wait(ProfilePageLocators.ORDER_HISTORY_FORM)

    @allure.step('Кликнуть на Выход')
    def click_logout_in_account(self):
        self.click_to_element(ProfilePageLocators.BUTTON_SECTION_LOGOUT)
        self.find_element_with_wait(LoginPageLocators.AUTO_FORM)



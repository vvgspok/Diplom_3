import allure
import pytest
from conftest import main_page
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators
from data import  user_data_for_login


class TestProfilePage:

    @allure.title('Тест перехода по клику на «Личный кабинет»')
    def test_click_go_to_personal_account(self, profile_page, login_page, main_page):
        login_page.auto_user(user_data_for_login["email"], user_data_for_login["password"])
        main_page.go_to_profile()
        element_form = profile_page.check_displaying_of_element(ProfilePageLocators.PROFILE_FORM)
        assert element_form == True

    @allure.title('Тест перехода в раздел «История заказов»')
    def test_go_to_order_history(self, profile_page, login_page, main_page):
        login_page.auto_user(user_data_for_login["email"], user_data_for_login["password"])
        main_page.go_to_profile()
        profile_page.click_go_to_order_history()
        element_form = profile_page.check_displaying_of_element(ProfilePageLocators.ORDER_HISTORY_FORM)
        assert element_form == True

    @allure.title('Тест выход из аккаунта')
    def test_logout_in_account(self, profile_page, login_page, main_page):
        login_page.auto_user(user_data_for_login["email"], user_data_for_login["password"])
        main_page.go_to_profile()
        profile_page.click_logout_in_account()
        element_form = profile_page.check_displaying_of_element(LoginPageLocators.AUTO_FORM)
        assert element_form == True
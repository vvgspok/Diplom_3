import allure
import pytest
from locators.recover_page_locators import RecoverPageLocators
from data import recover_page_button_text


class TestRecoverPage:

    @allure.title('Тест перехода на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_password_recover(self, recover_page):
        recover_page.go_to_page_password_recovery()
        element_form = recover_page.check_displaying_of_element(RecoverPageLocators.RECOVERY_FORM)
        element_text = recover_page.get_text_from_element(RecoverPageLocators.BUTTON_RECOVER)
        assert element_form == True and element_text == recover_page_button_text[0]

    @allure.title('Тест ввода почты и клик по кнопке «Восстановить»')
    def test_filling_email_and_click_recover_button(self, recover_page):
        recover_page.go_to_page_password_recovery()
        recover_page.submit_recovery_email()
        element_form = recover_page.check_displaying_of_element(RecoverPageLocators.RECOVERY_FORM)
        element_text = recover_page.get_text_from_element(RecoverPageLocators.BUTTON_SAVE)
        assert element_form == True and element_text == recover_page_button_text[1]

    @allure.title('Тест клика по кнопке показать/скрыть пароль подсвечивает поле')
    def test_password_visibility_toggle(self, recover_page):
        recover_page.go_to_page_password_recovery()
        recover_page.submit_recovery_email()
        recover_page.fill_password_and_code_field()
        recover_page.click_to_element(RecoverPageLocators.BUTTON_SHOW_PASSWORD)
        element = recover_page.check_displaying_of_element(RecoverPageLocators.ACTIVE_PASS_FIELD)
        assert element == True

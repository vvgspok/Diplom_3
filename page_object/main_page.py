from locators.order_feed_page_locators import OrderFeedPageLocators
from page_object.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from locators.header_page_locators import HeaderPageLocators
from locators.profile_page_locators import ProfilePageLocators


class MainPage(BasePage):

    @allure.step('Кликнуть на «Конструктор»')
    def go_to_constructor(self):
        self.click_to_element(HeaderPageLocators.BUTTON_CONSTRUCTOR)
        self.find_element_with_wait(MainPageLocators.BURGER_FORM)

    @allure.step('Кликнуть на «Лента заказов»')
    def go_to_order_feed(self):
        self.click_to_element(HeaderPageLocators.BUTTON_ORDER_FEED)
        self.find_element_with_wait(OrderFeedPageLocators.ORDER_FEED_FORM)

    @allure.step('Кликнуть на «Профиль»')
    def go_to_profile(self):
        self.click_to_element(HeaderPageLocators.BUTTON_PROFILE)
        self.find_element_with_wait(ProfilePageLocators.PROFILE_FORM)
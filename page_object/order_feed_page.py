from page_object.base_page import BasePage
import allure
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):

    @allure.step('Собрать бургер и оформить заказ')
    def create_burger_and_order(self):
        self.drag_and_drop(MainPageLocators.CLICK_INGREDIENTS, MainPageLocators.BURGER_BASKET)
        self.click_to_element(MainPageLocators.BUTTON_PLACE_AN_ORDER)
        text = self.get_text_from_element(MainPageLocators.BURGER_ORDER_ID)
        self.wait_until_the_specified_text_disappears(MainPageLocators.BURGER_ORDER_ID, text)
        get_order_id = self.get_text_from_element(MainPageLocators.BURGER_ORDER_ID)
        self.click_to_element(MainPageLocators.BUTTON_CLOSE_BURGER_MODAL)
        return get_order_id

    @allure.step('Нажать на заказ в ленте заказов')
    def click_to_order(self):
        self.click_to_element(OrderFeedPageLocators.CLICK_ORDER)
        self.find_element_with_wait(OrderFeedPageLocators.ORDER_MODAL)
















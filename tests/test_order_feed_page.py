from conftest import create_order
import pytest
import allure
from locators.order_feed_page_locators import OrderFeedPageLocators
from locators.order_history_page_locators import OrderPageHistoryLocators

class TestOrderFeedPage:


    @allure.title('Тест клик на заказ, открывает всплывающее окно с деталями')
    def test_click_order_to_show_details(self, order_feed_page, main_page, authorized_user):
        order_feed_page.create_burger_and_order()
        main_page.go_to_order_feed()
        order_feed_page.click_to_order()
        element = order_feed_page.check_displaying_of_element(OrderFeedPageLocators.ORDER_MODAL)
        assert element == True

    @allure.title('Тест отображение заказа пользователя в разделе «История заказов» и на странице «Лента заказов»')
    def test_compare_orders_in_feed_and_history(self, order_feed_page, create_order, main_page, profile_page, authorized_user):
        response = create_order
        order_num = response.json()["order"]["number"]
        main_page.go_to_profile()
        profile_page.click_go_to_order_history()
        element_order_number_in_profile = order_feed_page.wait_until_the_specified_text_appears(
            OrderPageHistoryLocators.ORDER_NUMBER, str(order_num))
        main_page.go_to_order_feed()
        element_order_number_in_order_feed = order_feed_page.wait_until_the_specified_text_appears(
            OrderFeedPageLocators.ORDER_NUM_FEED, str(order_num))
        assert element_order_number_in_profile == True and element_order_number_in_order_feed == True

    @allure.title('Тест увеличение счетчика "Выполнено за всё время" после создания нового заказа')
    def test_change_total_orders_counter(self, order_feed_page, main_page, authorized_user):
        main_page.go_to_order_feed()
        before_count = order_feed_page.get_text_from_element(OrderFeedPageLocators.ORDERS_FOR_ALL_TIME)
        main_page.go_to_constructor()
        order_id = order_feed_page.create_burger_and_order()
        main_page.go_to_order_feed()
        order_feed_page.wait_until_the_specified_text_appears(OrderFeedPageLocators.ORDERS_COMPLETED, order_id)
        after_count = order_feed_page.get_text_from_element(OrderFeedPageLocators.ORDERS_FOR_ALL_TIME)
        assert before_count < after_count

    @allure.title('Тест увеличение счетчика "Выполнено за сегодня" после создания нового заказа')
    def test_change_today_orders_counter(self, order_feed_page, main_page, authorized_user):
        main_page.go_to_order_feed()
        before_count = order_feed_page.get_text_from_element(OrderFeedPageLocators.ORDERS_FOR_TODAY)
        main_page.go_to_constructor()
        order_id = order_feed_page.create_burger_and_order()
        main_page.go_to_order_feed()
        order_feed_page.wait_until_the_specified_text_appears(OrderFeedPageLocators.ORDERS_COMPLETED, order_id)
        after_count = order_feed_page.get_text_from_element(OrderFeedPageLocators.ORDERS_FOR_TODAY)
        assert before_count < after_count

    @allure.title('Тест наличие номера нового заказа в разделе "В работе"')
    def test_order_in_progress(self, order_feed_page, main_page, authorized_user):
        main_page.go_to_constructor()
        order_id = order_feed_page.create_burger_and_order()
        main_page.go_to_order_feed()
        element = order_feed_page.wait_until_the_specified_text_appears(OrderFeedPageLocators.ORDERS_IN_PROGRESS, order_id)
        assert element == True

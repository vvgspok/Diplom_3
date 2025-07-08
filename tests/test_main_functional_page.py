import allure
import pytest
from data import URL, URL_ORDER_FEED
from locators.main_page_locators import MainPageLocators
from locators.order_feed_page_locators import OrderFeedPageLocators
from data import user_data_for_login

class TestMainFunctionalPage:

    @allure.title('Тест перехода по клику на «Конструктор»')
    def test_click_go_to_constructor(self, main_page):
        main_page.go_to_url(URL_ORDER_FEED)
        main_page.go_to_constructor()
        element_form = main_page.check_displaying_of_element(MainPageLocators.BURGER_FORM)
        assert element_form  == True

    @allure.title('Тест перехода по клику на «Лента заказов»')
    def test_click_go_to_order_feed(self, main_page, order_feed_page):
        main_page.go_to_url(URL)
        main_page.go_to_order_feed()
        element_form = order_feed_page.check_displaying_of_element(OrderFeedPageLocators.ORDER_FEED_FORM)
        assert element_form  == True

    @allure.title('Тест появления всплывающее окно с деталями, если кликнуть на ингредиент')
    def test_click_on_ingredient_opens_details_modal(self, main_page):
        main_page.go_to_url(URL)
        main_page.click_to_element(MainPageLocators.CLICK_INGREDIENTS)
        element_form = main_page.check_displaying_of_element(MainPageLocators.BURGER_MODAL)
        assert element_form == True

    @allure.title('Тест закрытия всплывающего окно с деталями при клике на крестик')
    def test_ingredient_modal_closes(self, main_page):
        main_page.go_to_url(URL)
        main_page.click_to_element(MainPageLocators.CLICK_INGREDIENTS)
        main_page.click_to_element(MainPageLocators.BUTTON_CLOSE_BURGER_MODAL)
        element_form = main_page.check_displaying_of_element(MainPageLocators.BURGER_MODAL)
        assert element_form == False

    @allure.title('Тест увеличения коунтера, при добавлении ингредиента в заказ')
    def test_add_ingredient_increases_counter(self, main_page):
        main_page.go_to_url(URL)
        main_page.drag_and_drop(MainPageLocators.CLICK_INGREDIENTS, MainPageLocators.BURGER_BASKET)
        counter_ingredient = int(main_page.get_text_from_element(MainPageLocators.INGREDIENTS_COUNTER))
        assert counter_ingredient == 2

    @allure.title('Тест залогиненный пользователь может оформить заказ')
    def test_authorized_user_can_create_order(self, main_page, login_page):
        login_page.auto_user(user_data_for_login["email"], user_data_for_login["password"])
        main_page.drag_and_drop(MainPageLocators.CLICK_INGREDIENTS, MainPageLocators.BURGER_BASKET)
        main_page.click_to_element(MainPageLocators.BUTTON_PLACE_AN_ORDER)
        element_9999 = main_page.get_text_from_element(MainPageLocators.BURGER_ORDER_ID)
        main_page.wait_until_the_specified_text_disappears(MainPageLocators.BURGER_ORDER_ID, element_9999)
        element_id = main_page.get_text_from_element(MainPageLocators.BURGER_ORDER_ID)
        assert element_id != element_9999
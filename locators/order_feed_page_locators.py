from selenium.webdriver.common.by import By

class OrderFeedPageLocators:

    ORDER_FEED_FORM = By.XPATH, "//*[contains(@class, 'OrderFeed_contentBox')]"
    TEXT_ORDER_FEED = By.XPATH, "//*[text()='Лента заказов']"
    CLICK_ORDER = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem_')][1]"
    ORDER_MODAL = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/child::div[1]"
    ORDER_NUM_FEED = By.XPATH, "//*[contains(@class, 'OrderHistory_textBox__')]/p[1]"

    ORDERS_FOR_ALL_TIME = By.XPATH, "//*[text()='Выполнено за все время:']/following-sibling::p"
    ORDERS_COMPLETED = By.XPATH, "//*[text()='Готовы:']/following-sibling::ul[1]/li"
    ORDERS_IN_PROGRESS = By.XPATH, "//*[text()='В работе:']/following-sibling::ul[2]/li"

    ORDERS_FOR_TODAY = By.XPATH, "//*[text()='Выполнено за сегодня:']/following-sibling::p"
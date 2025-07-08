from selenium.webdriver.common.by import By

class OrderPageHistoryLocators:

    ORDER_NUMBER = By.XPATH, "//*[contains(@class, 'OrderHistory_profileList_')]/descendant::p[1]"
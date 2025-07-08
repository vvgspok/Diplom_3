from selenium.webdriver.common.by import By

class ProfilePageLocators:


    BUTTON_SECTION_PROFILE = By.XPATH, "//*[text()='Профиль']"
    PROFILE_FORM = By.XPATH, "//*[contains(@class, 'Profile_profile_')]"
    NAME_INPUT_FIELD_LOGIN = By.XPATH, "//*[text()='Логин']"

    BUTTON_SECTION_ORDER_HISTORY= By.XPATH, "//*[text()='История заказов']"
    ORDER_HISTORY_FORM = By.XPATH, "//*[contains(@class, 'OrderHistory_orderHistory')]"

    BUTTON_SECTION_LOGOUT = By.XPATH, "//*[text()='Выход']"
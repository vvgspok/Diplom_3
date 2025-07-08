from selenium.webdriver.common.by import By


class LoginPageLocators:

    TEXT_LOGIN = By.XPATH, "//*[text()='Вход']"
    INPUT_FIELD_EMAIL = By.XPATH, "//*[@name='name']"
    INPUT_FIELD_PASS = By.XPATH, "//*[@name='Пароль']"
    BUTTON_LOGIN = By.XPATH, "//*[text()='Войти']"
    AUTO_FORM = By.XPATH, "//*[contains(@class, 'Auth_form')]"

    BUTTON_RECOVER_PASSWORD = By.XPATH, "//*[text()='Восстановить пароль']"

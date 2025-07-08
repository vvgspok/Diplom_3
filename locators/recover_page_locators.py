from selenium.webdriver.common.by import By

class RecoverPageLocators:


    INPUT_FIELD_EMAIL = By.XPATH, "//*[@name='name']"
    BUTTON_RECOVER = By.XPATH, "//*[text()='Восстановить']"

    RECOVERY_FORM = By.XPATH, "//*[contains(@class, 'Auth_form')]"

    RECOVER_FORM_NAME = By.XPATH, "//*[text()='Восстановление пароля']"
    INPUT_FIELD_PASSWORD = By.XPATH, "//*[@name='Введите новый пароль']"
    INPUT_FIELD_CODE = By.XPATH, "//*[@name='name']"
    BUTTON_SAVE = By.XPATH, "//*[text()='Сохранить']"
    BUTTON_SHOW_PASSWORD = By.XPATH, "//*[@name='Введите новый пароль']/following::div[1]/*"
    ACTIVE_PASS_FIELD = By.XPATH, "//*[text()='Пароль']/parent::div[contains(@class, 'input_status_active')]"
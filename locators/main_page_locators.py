from selenium.webdriver.common.by import By


class MainPageLocators:

    BUTTON_LOGIN = By.XPATH, "//*[text()='Войти в аккаунт']"
    BURGER_FORM = By.XPATH, "//*[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]"
    TEXT_BURGER = By.XPATH, "//*[text()='Соберите бургер']"

    CLICK_INGREDIENTS = By.XPATH, "//*[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]/descendant::a[1]"
    INGREDIENTS_COUNTER = By.XPATH, "//*[contains(@class, 'BurgerIngredients_ingredients__menuContainer')]/descendant::p[1]"
    TEXT_BURGER_MODAL = By.XPATH, "//*[text()='Детали ингредиента']"
    BURGER_MODAL = By.XPATH, "//*[contains(@class, 'Modal_modal_opened')]/child::div[1]"
    BUTTON_CLOSE_BURGER_MODAL = By.XPATH, "//*[contains(@class,'Modal_modal_opened')]/descendant::button"
    MODAL_OVERLAY = By.XPATH, "//*[contains(@class, 'Modal_modal__loading_')]/following-sibling::div"

    BURGER_BASKET = By.XPATH, "//section[contains(@class, 'BurgerConstructor_basket_')]"

    BUTTON_PLACE_AN_ORDER = By.XPATH, "//*[text()='Оформить заказ']"

    BURGER_ORDER_ID = By.XPATH, "//*[contains(@class, 'Modal_modal__title_shadow_')]"


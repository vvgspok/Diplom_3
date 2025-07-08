from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import allure
from data import browser_name
from locators.main_page_locators import MainPageLocators


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(
            expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def wait_until_the_specified_text_disappears(self, locator, text):
        self.wait.until_not(
            expected_conditions.text_to_be_present_in_element(locator, text)
        )

    def wait_until_the_specified_text_appears(self, locator, text):
        return self.wait.until(
            expected_conditions.text_to_be_present_in_element(locator, text)
            )

    def click_to_element(self, locator):
        self.wait.until_not(
            expected_conditions.visibility_of_element_located(MainPageLocators.MODAL_OVERLAY))
        element = self.check_element_is_clickable(locator)
        if browser_name == 'Firefox':
            ActionChains(self.driver).move_to_element(element).click().perform()
        else:
           element.click()


    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text


    def check_element_is_clickable(self, locator):
        return  self.wait.until(expected_conditions.element_to_be_clickable(locator))


    def check_displaying_of_element(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except NoSuchElementException:
            return False


    def drag_and_drop(self, locator_from, locator_to):
        script = """
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);

                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
            """
        elem_from = self.find_element_with_wait(locator_from)
        elem_to = self.find_element_with_wait(locator_to)
        self.driver.execute_script(script, elem_from, elem_to)




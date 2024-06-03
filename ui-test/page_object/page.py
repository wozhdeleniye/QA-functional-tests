from .locators import MainPageLocators

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):
    def is_title_matches(self):
        return "Erase Overlap Intervals" == self.driver.title
    def fill_data(self, data):
        string_element = self.driver.find_element(*MainPageLocators.STRING_INPUT)
        string_element.send_keys(data)
    def click_send_button(self):
        send_button = self.driver.find_element(*MainPageLocators.SEND_BUTTON)
        send_button.click()
    def get_result(self):
        result_element = self.driver.find_element(*MainPageLocators.RESULT_OUTPUT)
        return result_element.text

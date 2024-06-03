from selenium.webdriver.common.by import By

class MainPageLocators(object):
    STRING_INPUT = (By.ID, "string")
    SEND_BUTTON = (By.ID, "submit")
    RESULT_OUTPUT = (By.ID, "result")
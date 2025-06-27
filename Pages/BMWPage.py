from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader

class BMWPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)
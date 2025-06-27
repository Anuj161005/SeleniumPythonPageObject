from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Utilities import configReader

class NewCarsPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def selectMahindra(self):
        self.click("mahindra_XPATH")

    def selectTata(self):
        self.click("tata_XPATH")

    def selectHyundai(self):
        self.click("hyundai_XPATH")

    def selectBMW(self):
        self.click("BMW_XPATH")
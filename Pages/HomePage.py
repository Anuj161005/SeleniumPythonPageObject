from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage
from Utilities import configReader

class HomePage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newCar_XPATH")
        self.click("findNewCar_XPATH")

        return NewCarsPage(self.driver)

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass
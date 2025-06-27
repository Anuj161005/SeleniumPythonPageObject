import time

import allure
import openpyxl
import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Pages.RegistrationPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataprovider
import logging
from Utilities.LogUtil import Logger
log = Logger(__name__,logging.INFO)
class Test_carwale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCars(self):
        log.logger.info("*********Inside New Car Test**********")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle", dataprovider.get_data("NewCarsTest"))
    def test_selectCars(self, carBrand,carTitle):
        log.logger.info("*********Inside Select Cars Test**********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        if carBrand == "Mahindra":
            home.gotoNewCars().selectMahindra()
            title = car.getCarTitle()
            print("car title is: ",title)
            assert title == carTitle,"The title is not matching"
        elif carBrand == "Tata":
            home.gotoNewCars().selectTata()
            title = car.getCarTitle()
            print("car title is: ", title)
            assert title == carTitle, "The title is not matching"

        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("car title is: ", title)
            assert title == carTitle, "The title is not matching"

        elif carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print(("car title is: "+title).encode('utf8'))
            assert title == carTitle, "The title is not matching"



    @pytest.mark.parametrize("carBrand,carTitle", dataprovider.get_data("NewCarsTest"))
    def test_carNamesAndPrices(self, carBrand, carTitle):
        log.logger.info("*********Inside Cars names and prices Test**********")
        home = HomePage(self.driver)
        car = CarBase(self.driver)
        #path = "../Excel/testData.xlsx"
        #sheetname = "UploadData"
        if carBrand == "Mahindra":
            home.gotoNewCars().selectMahindra()
            title = car.getCarTitle()
            print(("car title is: "+title).encode('utf8git'))
            assert title == carTitle, "The title is not matching"
            car.carNameAndPrices()
            # car.carNameAndPrices(path,sheetname)
        elif carBrand == "Tata":
            home.gotoNewCars().selectTata()
            title = car.getCarTitle()
            print(("car title is: "+title).encode('utf8'))
            assert title == carTitle, "The title is not matching"
            car.carNameAndPrices()
            # car.carNameAndPrices(path,sheetname)

        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("car title is: "+title).encode('utf8'))
            assert title == carTitle, "The title is not matching"
            car.carNameAndPrices()
            # car.carNameAndPrices(path,sheetname)

        elif carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print(("car title is: "+title).encode('utf8'))
            assert title == carTitle, "The title is not matching"
            car.carNameAndPrices()
            # car.carNameAndPrices(path,sheetname)








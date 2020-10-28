from selenium import webdriver
import pytest
import time
from PageObjects.LoginPage import LoginPage


class Test_001_Login:




    def test_homePageTitle(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        act_title=self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else :
            assert False
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homePageTitle.png")


    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        # self.driver.implicitly_wait(10)
        act_title=self.driver.title

        if act_title == "Dashboard opCommerce administration":
            assert True
            self.driver.close()

        else:

            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            assert False


        # self.lp.clickLogout(self)
        # act_title=self.driver.title

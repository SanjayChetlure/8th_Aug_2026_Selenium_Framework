import time
from selenium import webdriver

from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage


class Test_SwagLabLogin:

    def test_TC1_loginWithValidData(self,setup):
        driver=setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName("standard_user")
        time.sleep(2)
        loginObj.enterPassword("secret_sauce")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        time.sleep(3)

        homeObj = SwagLabHomePage(driver)
        actLogoText = homeObj.getLogoText()
        expLogoText = "Swag Labs"

        if actLogoText == expLogoText:
            print("Login Test is Passed")
        else:
            print("Login Test is Failed")

        time.sleep(2)
        driver.quit()

    def test_TC2_loginWithInvalidData(self,setup):
        driver=setup

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName("abc")
        time.sleep(2)
        loginObj.enterPassword("xyz")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        time.sleep(3)
        actLoginFailedErrorMsg = loginObj.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            print("Login Failed Test is Passed")
        else:
            print("Login Failed Test is Failed")


        time.sleep(3)
        driver.quit()


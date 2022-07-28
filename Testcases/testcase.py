import pytest
from pageobjects.loginpage import Login
from utilities.readproperties import Readconfig
from utilities.customlogger import Loggen
import pytest_html
class Test_001_login:
    baseurl = Readconfig.getapplicationurl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    logger= Loggen.loggen()

    def test_homepagetitle(self, setup):
        self.logger.info("+++++++++++Test_001_login++++++++++++++")
        self.logger.info("+++++++++++verifying test home page++++++++++++++")

        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.logger.info("+++++++++++test home page passed++++++++++++++")

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"testhomepage.png")
            assert False
        self.driver.close()

    def test_login(self, setup):
        self.logger.info("+++++++++++test login started++++++++++++++")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("+++++++++++test login passed++++++++++++++")

        else:
            assert False
        self.driver.close()


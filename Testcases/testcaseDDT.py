import pytest
from pageobjects.loginpage import Login
from utilities.readproperties import Readconfig
from utilities.customlogger import Loggen
import pytest_html
from utilities import XLutils
import time

class Test_002_DDT_login:
    baseurl = Readconfig.getapplicationurl()
    path=".//test data/nopselenium.xlsx"
    logger= Loggen.loggen()

    def test_login_ddt(self, setup):
        self.logger.info("+++++++++++Test_002_DDT_login++++++++++++++")
        self.logger.info("+++++++++++test login started++++++++++++++")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp = Login(self.driver)
        self.driver.implicitly_wait(5)
        self.rows=XLutils.getrowcount(self.path,'Sheet1')
        print("number of rows in the excel file", self.rows)

        lst_status = []
        for r in range(2, self.rows+1):
            self.user=XLutils.readdata(self.path,'Sheet1',r,1)
            self.password=XLutils.readdata(self.path, 'Sheet1', r, 2)
            self.exp=XLutils.readdata(self.path, 'Sheet1', r, 3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.clicklogin()
            time.sleep(5)
            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title==exp_title:
                if self.exp=="Pass":
                    self.logger.info("*******passed after correct credentials")
                    self.lp.clicklogout()
                    lst_status.append("Pass")
                elif self.exp=="Fail":
                    self.logger.info("*******Failed after correct credentials")
                    self.lp.clicklogout()
                    lst_status.append("Fail")
            elif act_title!=exp_title:
                if self.exp=="Pass":
                    self.logger.info("*******failed in incorrect credentials")
                    lst_status.append("Fail")
                elif self.exp=="Fail":
                    self.logger.info("*******passed")
                    lst_status.append("Pass")
        if "Fail" not in lst_status:
            self.logger.info("*******login DDT test passed*******")
            assert True
        else:
            self.logger.info("*******login DDT test failed*******")
            assert False
        self.driver.close()
        self.logger.info("*******End of Login DDT test*******")






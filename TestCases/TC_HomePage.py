import selenium
from selenium import webdriver
import unittest
import HtmlTestRunner
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
import sys
sys.path.append('C:/Users/Admin/PycharmProjects/Nhom19AutomationTest')
from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage

class HomePageTest(unittest.TestCase):
    baseURL = 'http://localhost:3000/'
    email = '20110752@student.hcmute.edu.vn'
    passwd = 'okbabylady0'
    liveAssertText = 'Inbound - General Europe'
    inboundAssertText = 'Inbound - General Europe'
    serviceLevelsAssertText = 'Inbound - General Europe'
    agentsAssertText = 'Inbound - General Europe'
    numbersAssertText = 'Phone Number Metrics'
    logOutAssertText = 'Forgot your password'
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\Nhom19AutomationTest\\Drivers\pythchromedriver.exe")
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)

    # Test Option: Chọn Live của thanh header
    def test01(self):
        # Login into HomePage:
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        login.setPasswd(self.passwd)
        login.clickLogin()
        time.sleep(2)

        # Initialize homepage testing
        homepage = HomePage(self.driver)
        homepage.clickLive()
        self.assertTrue(self.liveAssertText,homepage.getLiveAssertText())
        homepage.clickLogOut()
        time.sleep(1)
        print('Test Option: Chon Live cua thanh header')

    # Test Option: Chọn Inbound của thanh header
    def test02(self):
        # Login into HomePage:
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        login.setPasswd(self.passwd)
        login.clickLogin()
        time.sleep(2)

        # Initialize homepage testing
        homepage = HomePage(self.driver)
        homepage.clickInbound()
        self.assertTrue(self.inboundAssertText, homepage.getInboundAssertText())
        homepage.clickLogOut()
        time.sleep(1)
        print('Test Option: Chon Inbound cua thanh header')
    # Test Option: Chọn Service Level của thanh header
    def test03(self):
        # Login into HomePage:
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        login.setPasswd(self.passwd)
        login.clickLogin()
        time.sleep(2)

        # Initialize homepage testing
        homepage = HomePage(self.driver)
        homepage.clickInbound()
        self.assertTrue(self.serviceLevelsAssertText, homepage.getServiceLevelAssertText())
        homepage.clickLogOut()
        time.sleep(1)
        print('Test Option: Chon Service Level cua thanh header')

    # Test Option: Chọn Agents  của thanh header
    def test04(self):
        # Login into HomePage:
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        login.setPasswd(self.passwd)
        login.clickLogin()
        time.sleep(2)

        # Initialize homepage testing
        homepage = HomePage(self.driver)
        homepage.clickAgents()
        self.assertTrue(self.agentsAssertText, homepage.getAgentsAssertText())
        homepage.clickLogOut()
        time.sleep(1)
        print('Test Option: Chon Agents  cua thanh header')
    # Test Option: Chọn Numbers  của thanh header
    def test05(self):
        # Login into HomePage:
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        login.setPasswd(self.passwd)
        login.clickLogin()
        time.sleep(2)

        # Initialize homepage testing
        homepage = HomePage(self.driver)
        homepage.clickNumbers()
        self.assertTrue(self.numbersAssertText, homepage.getNumbersAssertText())
        homepage.clickLogOut()
        time.sleep(1)
        print('Test Option: Chon Numbers  cua thanh header')

    # Test Đăng Xuất: chức năng đăng xuất
    def test06(self):
        self.driver.get(self.baseURL)
        # Login into HomePage:
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        login.setPasswd(self.passwd)
        login.clickLogin()
        time.sleep(2)

        # Initialize homepage's logout testing
        homepage = HomePage(self.driver)
        homepage.clickLogOut()
        self.assertTrue(self.logOutAssertText,homepage.getLogOutAssertText())

        print('Test Dang Xuat: chuc nang dang xuat')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # tat browser
        print('FINISHED TEST')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports/'))
    # unittest.main()
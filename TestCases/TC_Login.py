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
from PagesObjects.LoginPage import LoginPage




class LoginTest(unittest.TestCase):
    baseURL = 'http://localhost:3000/'
    email = '20110752@student.hcmute.edu.vn'
    emailCaNhan = 'binclun2002@gmail.com'
    email2 = 'Nhom19@student.hcmute.edu.vn'
    passwd = 'okbabylady0'
    studentPasswd = 'okbabylady='
    passwd2 = 'nhom19'
    passwdCaNhan = 'okbabylady'
    assertionText = 'Inbound - General Europe'
    assertionAlert = 'Đăng nhập thất bại...'
    assertionAlert2 = 'Vui lòng đăng nhập bằng email sinh viên'
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\Nhom19AutomationTest\\Drivers\pythchromedriver.exe")

    # open browser
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()

    # Test Đăng Nhập: Username và password khớp với Database, Click nút "Đăng nhập"
    def test01(self):
            login = LoginPage(self.driver)  ## khoi tao webdriver
            login.setEmail(self.email)
            login.setPasswd(self.passwd)
            login.clickLogin()
            time.sleep(2)  # sleep
            self.assertTrue(self.assertionText == login.getAssertText())
            login.clickLogout()
            print('TEST1 PASSED')

    # Test Đăng Nhập: Username và password không khớp với Database, Click nút "Đăng nhập"
    def test02(self):
            login = LoginPage(self.driver)  # khoi tao webdriver
            login.setEmail('')  # email trong
            login.setEmail(self.email2)  # email sai
            login.setPasswd('')  # pass trong
            login.setPasswd(self.passwd2)  # pass sai

            login.clickLogin()
            time.sleep(1)  # sleep

        # Switch to the alert and get its text
            alert = Alert(self.driver)
            alert_text = alert.text

        # Assert that the alert text is as expected

            self.assertTrue(self.assertionAlert == alert.text)

    # Close the alert
            alert.accept()

    # login.clickLogout()
            print('TEST2 PASSED')


# Test Đăng Nhập: Username để trống, Click nút "Đăng nhập"
    def test03(self):
            login = LoginPage(self.driver)  # khoi tao webdriver
            login.setEmail('')  # email sai
            login.setPasswd(self.passwd2)  # pass sai

            login.clickLogin()
            time.sleep(1)  # sleep

    # Switch to the alert and get its text
            alert = Alert(self.driver)
            alert_text = alert.text

    # Assert that the alert text is as expected
            self.assertTrue(self.assertionAlert == alert.text)

    # Close the alert
            alert.accept()

    # login.clickLogout()
            print('TEST3 PASSED')


# Test Đăng Nhập: Password để trống, Click nút "Đăng nhập"
    def test04(self):
            login = LoginPage(self.driver)  # khoi tao webdriver
            login.setEmail(self.email2)  # email
            login.setPasswd('')  # pass trong

            login.clickLogin()
            time.sleep(1)  # sleep

    # Switch to the alert and get its text
            alert = Alert(self.driver)
            alert_text = alert.text

    # Assert that the alert text is as expected
            self.assertTrue(self.assertionAlert == alert.text)

    # Close the alert
            alert.accept()

    # login.clickLogout()
            print('TEST4 PASSED')


# Test Đăng Nhập: Username và password để trống, Click nút "Đăng nhập"
    def test05(self):
            login = LoginPage(self.driver)  # khoi tao webdriver
            login.setEmail('')  # email trong
            login.setPasswd('')  # pass trong

            login.clickLogin()
            time.sleep(1)  # sleep

    # Switch to the alert and get its text
            alert = Alert(self.driver)
            alert_text = alert.text

    # Assert that the alert text is as expected
            self.assertTrue(self.assertionAlert == alert.text)

    # Close the alert
            alert.accept()

    # login.clickLogout()
            print('TEST5 PASSED')
    #Test Đăng Nhập: Username và password để trống, Click nút "Enter"
    def test06(self):
            login = LoginPage(self.driver)  # khoi tao webdriver
            login.setEmail('')  # email trong
            login.setPasswd('')  # pass trong

            login.pressEnter()
            time.sleep(1)  # sleep

        # Switch to the alert and get its text
            alert = Alert(self.driver)
            alert_text = alert.text

        # Assert that the alert text is as expected
            self.assertTrue(self.assertionAlert == alert.text)

        # Close the alert
            alert.accept()

        # login.clickLogout()
            print('TEST6 PASSED')
    #Test Đăng Nhập: Bằng Google tài khoản của sinh viên, Click nút "Đăng nhập"
    def test07(self):
            login = LoginPage(self.driver)
            login.clickGoogle(self.email,self.studentPasswd)
            time.sleep(2)  # sleep
            self.assertTrue(self.assertionText == login.getAssertText())
            login.clickLogout()
            print('TEST7 PASSED')

    #Test Đăng Nhập: Bằng Google tài khoản không phải của sinh viên, Click nút "Đăng nhập"
    def test08(self):
            login = LoginPage(self.driver)
            login.clickGoogle(self.emailCaNhan, self.passwdCaNhan)
            time.sleep(2)  # sleep

            # Switch to the alert and get its text
            alert = Alert(self.driver)
            alert_text = alert.text

        # Assert that the alert text is as expected
            self.assertTrue(self.assertionAlert2 == alert.text)

        # Close the alert
            alert.accept()
            print('TEST8 PASSED')





    # Tat WebDriver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # tat browser
        print('FINISHED TEST')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports/'))
    #unittest.main()

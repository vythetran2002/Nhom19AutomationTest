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

class RegisterTest(unittest.TestCase):
    baseURL = 'http://localhost:3000/'
    name = 'Nhom19'
    email = '20110752@student.hcmute.edu.vn'
    email2 = '20110751@student.hcmute.edu.vn'
    passwd2 = 'nhom19'
    passwd = 'okbabylady0'
    assertionAlert01 = 'Email đã tồn tại'
    assertionAlert02 = 'Mã xác thực đã được gửi qua email: '+email2
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\Nhom19AutomationTest\\Drivers\pythchromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)

    # Test Đăng ký: Họ tên khớp, email, password khớp với Database, Click nút "Đăng ký"
    def test01(self):
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName(self.name)
        register.setRegisterEmail(self.email)
        register.setRegisterPasswd(self.passwd)
        register.clickRegister()
        time.sleep(3)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert01 == alert.text)

        # Close the alert
        alert.accept()

        print('Test Dang ky: Ho ten khop, email, password khop voi Database, Click nut Dang ky: Passed')

    # Test Đăng ký: Họ tên khớp, email với Database và password không khớp với Database, Click nút "Đăng ký"
    def test02(self):
        self.driver.get(self.baseURL)
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName(self.name)
        register.setRegisterEmail(self.email2)
        register.setRegisterPasswd(self.passwd2)
        register.clickRegister()
        time.sleep(5)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert02 == alert.text)

        # Close the alert
        alert.accept()

        print('Test Dang ky: Ho ten khop, email voi Database va password khong khop voi Database, Click nut Dang ky: Passed')

    # Test Đăng ký: Họ tên khớp với Database và email, password không khớp với Database, Click nút "Đăng ký"
    def test03(self):
        self.driver.get(self.baseURL)
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName(self.name)
        register.setRegisterEmail(self.email2)
        register.setRegisterPasswd(self.passwd2)
        register.clickRegister()
        time.sleep(5)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert02 == alert.text)

        # Close the alert
        alert.accept()

        print('Test Dang ky: Ho ten khop voi Database va email, password khong khop voi Database, Click nut Dang ky: Passed')

    # Test Đăng ký: Họ tên, email, password không khớp với Database, Click nút "Đăng ký"
    def test04(self):
        self.driver.get(self.baseURL)
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName('test04')
        register.setRegisterEmail(self.email2)
        register.setRegisterPasswd(self.passwd2)
        register.clickRegister()
        time.sleep(5)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert02 == alert.text)

        # Close the alert
        alert.accept()

        print('Test Dang ky: Ho ten, email, password khong khop voi Database, Click nut Dang ky: Passed')

    # Test Đăng ký: Email khớp với Database và họ tên, password không khớp với Database, Click nút "Đăng ký"
    def test05(self):
        self.driver.get(self.baseURL)
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName('test05')
        register.setRegisterEmail(self.email)
        register.setRegisterPasswd(self.passwd2)
        register.clickRegister()
        time.sleep(3)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert01 == alert.text)

        # Close the alert
        alert.accept()

        print('Test Dang ky: Email khop voi Database va ho ten, password khong khop voi Database, Click nut Dang ky: Passed')

    # Test Đăng ký: Email, password khớp với Database và họ tên không khớp với Database, Click nút "Đăng ký"
    def test06(self):
        self.driver.get(self.baseURL)
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName('test06')
        register.setRegisterEmail(self.email)
        register.setRegisterPasswd(self.passwd)
        register.clickRegister()
        time.sleep(3)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert01 == alert.text)

        # Close the alert
        alert.accept()

        print(' Test Dang ky: Email, password khop voi Database va ho ten khong khop voi Database, Click nut Dang ky: Passed')

    # Test Đăng ký: Password khớp với Database và họ tên, email không khớp với Database, Click nút "Đăng ký"
    def test07(self):
        self.driver.get(self.baseURL)
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName('test07')
        register.setRegisterEmail(self.email2)
        register.setRegisterPasswd(self.passwd)
        register.clickRegister()
        time.sleep(4)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert02 == alert.text)

        # Close the alert
        alert.accept()

        print(' Test Dang ky: Password khop voi Database va ho ten, email khong khop voi Database, Click nut Dang ky: Passed')

    # Test Đăng ký: Password, họ tên khớp với Database và email không khớp với Database, Click nút "Đăng ký"
    def test08(self):
        self.driver.get(self.baseURL)
        register = LoginPage(self.driver)
        register.clickSignUp()
        register.setRegisterName(self.name)
        register.setRegisterEmail(self.email2)
        register.setRegisterPasswd(self.passwd)
        register.clickRegister()
        time.sleep(6)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert02 == alert.text)

        # Close the alert
        alert.accept()

        print('Test Dang ky: Password, ho ten khop voi Database va email khong khop voi Database, Click nut Dang ky: Passed')
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # tat browser
        print('FINISHED TEST')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports/'))
    # unittest.main()
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
from PagesObjects.AdminPage import AdminPage

class AdminTest(unittest.TestCase):

    nameTest = 'test05'
    passwdTest = 'test05'
    emailTest = 'test05@gmail.com'
    baseURL = 'http://localhost:3000/'
    email = 'admin@admin'
    passwd = '1'
    assertTextLogin = 'Inbound - General Europe'
    assertAlertAddStaff = 'Thêm nhân viên thành công'
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\Nhom19AutomationTest\\Drivers\pythchromedriver.exe")
    nameSearchTest = 'Linh'
    assertEdit = 'Chỉnh sửa nhân viên thành công'
    assertDelete = 'Dữ liệu nhân viên chưa được khởi tạo!!!'

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)

    #TEST: Dang nhap bang tai khoan admin
    def test01(self):
        login = LoginPage(self.driver)
        login.setEmail(self.email)
        login.setPasswd(self.passwd)
        login.clickLogin()
        time.sleep(2)

        admin = AdminPage(self.driver)
        self.assertTrue(admin.getAssertLogin() == self.assertTextLogin)

        print('Dang nhap bang tai khoan admin: PASSED')

    #TEST: Them Nhan vien bang tai khoan admin
    def test02(self):

        # #Login into Admin account
        # login = LoginPage(self.driver)
        # login.setEmail(self.email)
        # login.setPasswd(self.passwd)
        # login.clickLogin()
        # time.sleep(3)

        #initial testing
        admin = AdminPage(self.driver)
        admin.clickAddStaff()
        time.sleep(3)
        admin.setNameAddStaff(self.nameTest)
        admin.setEmailAddStaff(self.emailTest)
        admin.setPasswdAddStaff(self.passwdTest)
        admin.clickAddStaffFinal()

        time.sleep(3)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected
        self.assertTrue(self.assertAlertAddStaff == alert.text)

        # Close the alert
        alert.accept()

        print('Them Nhan vien bang tai khoan admin: PASSED')

    #Test: Tim kiem nhan vien bang tai khoan admin
    def test03(self):
        self.driver.get(self.baseURL)
        # Login into Admin account
        # login = LoginPage(self.driver)
        # login.setEmail(self.email)
        # login.setPasswd(self.passwd)
        # login.clickLogin()
        # time.sleep(1)

        # initial testing
        admin = AdminPage(self.driver)
        admin.setNameSearchStaff(self.nameSearchTest)
        admin.clickSearch()
        time.sleep(2)

        self.assertTrue(self.nameSearchTest == admin.getAssertSearch())

        print('Tim kiem nhan vien bang tai khoan admin: PASSED')

    #Test: Chinh sua thong tin nhan vien bang tai khoan admin
    def test04(self):
        self.driver.get(self.baseURL)
        # # Login into Admin account
        # login = LoginPage(self.driver)
        # login.setEmail(self.email)
        # login.setPasswd(self.passwd)
        # login.clickLogin()
        # time.sleep(1)

        # Search for Staff by Staff's name
        admin = AdminPage(self.driver)
        admin.setNameSearchStaff(self.nameTest)
        admin.clickSearch()
        time.sleep(2)

        # initial testing
        admin.clickEditStaff()
        time.sleep(2)
        self.nameTest = self.nameTest + '_Edited'
        admin.setNameEditStaff(self.nameTest)
        admin.clickEditStaffFinal()
        time.sleep(2)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected
        self.assertTrue(self.assertEdit == alert.text)

        # Close the alert
        alert.accept()

        print('Chinh sua thong tin nhan vien bang tai khoan admin: PASSED')

    #Test: Xoa nhan vien bang tai khoan admin
    def test05(self):
        self.driver.get(self.baseURL)
        # # Login into Admin account
        # login = LoginPage(self.driver)
        # login.setEmail(self.email)
        # login.setPasswd(self.passwd)
        # login.clickLogin()
        # time.sleep(1)

        # Search for Staff by Staff's name
        admin = AdminPage(self.driver)
        admin.setNameSearchStaff(self.nameTest)
        admin.clickSearch()
        time.sleep(2)

        #Initial testing
        admin.clickDeleteStaff()
        time.sleep(2)

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        # Close the alert
        alert.accept()

        #Searching again then assert
        admin.setNameSearchStaff(self.nameTest)
        admin.clickSearch()
        time.sleep(2)
        self.assertTrue(self.assertDelete == admin.getAssertDelete())

        print('Xoa nhan vien bang tai khoan admin: Passed')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # tat browser
        print('FINISHED TEST')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports/'))
    #unittest.main()
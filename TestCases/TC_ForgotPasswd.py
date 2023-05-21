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

class ForgotPasswdTest(unittest.TestCase):
    baseURL = 'http://localhost:3000/'
    email = '20110752@student.hcmute.edu.vn'
    email2 = '20110999@student.hcmute.edu.vn'
    email3 = 'nhom19@gmail.com'
    assertionAlert = 'Đã gửi mật khẩu mới qua email'
    assertionAlert2 = 'Email đã tồn tại'
    assertionAlert3 = 'Vui lòng nhập email sinh viên'
    assertionAlert4 = 'Bạn nhập sai mã OTP'
    assertionAlert5 = 'Đăng nhập thất bại...'
    assertionAlert6 = 'Mã xác thực đã được gửi qua email: ' + email
    assertionText = 'Inbound - General Europe'
    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\Nhom19AutomationTest\\Drivers\pythchromedriver.exe")
    # open browser
    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseURL)


    # Test quên mật khẩu : Nhập email sinh viên khớp với email trong database
    def test01(self):
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail(self.email)
        forgotPass.clickOutside()
        time.sleep(5)

        #xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert6 == alert.text)
        alert.accept()

        print('Test quen mat khau : Nhap email sinh vien khop voi email trong database: PASSED')


    # Test quên mật khẩu : Nhập email sinh viên không khớp với email trong database
    def test02(self):
        self.driver.get(self.baseURL)
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail(self.email2)
        time.sleep(3)
        forgotPass.clickOutside()
        time.sleep(3)

        # xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert2 == alert.text)
        alert.accept()

        print('Test quen mat khau : Nhap email sinh vien khong khop voi email trong database: PASSED')

    #Test quên mật khẩu : Nhập email cá nhân
    def test03(self):
        self.driver.get(self.baseURL)
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail('')
        forgotPass.setForgotEmail(self.email3)
        forgotPass.clickOutside()
        time.sleep(3)

        # xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert3 == alert.text)
        alert.accept()

        print('Test quen mat khau : Nhap email ca nhan: PASSED')

    #Test quên mật khẩu : Nhập sai mã OTP nhận từ email
    def test04(self):
        self.driver.get(self.baseURL)
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail(self.email)
        forgotPass.clickOutside()
        time.sleep(5)

        # Thoat Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        # Lay OTP va nhap
        otp = forgotPass.getOTP()
        print(otp)
        forgotPass.setOTP('nhom19')
        forgotPass.clickOutside()
        time.sleep(5)

        # xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert4 == alert.text)
        alert.accept()

        print('Test quen mat khau : Nhap sai ma OTP nhan tu email: PASSED')

    # Test quên mật khẩu : Nhập đúng mã OTP của đúng email cần lấy lại tài khoản
    def test05(self):
        self.driver.get(self.baseURL)
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail(self.email)
        forgotPass.clickOutside()
        time.sleep(5)

        # Thoat Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        # Lay OTP va nhap
        otp = forgotPass.getOTP()
        print(otp)
        forgotPass.setOTP(otp)
        forgotPass.clickOutside()
        time.sleep(5)

        # xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert == alert.text)
        alert.accept()

        print('Test quen mat khau : Nhap dung ma OTP cua dung email can lay lai tai khoan: PASSED')

    # Test quên mật khẩu : Nhập đúng mã OTP của email khác
    def test06(self):
        self.driver.get(self.baseURL)
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail(self.email)
        forgotPass.clickOutside()
        time.sleep(5)

        # Thoat Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        # Lay OTP va nhap
        otp = forgotPass.getOTP()
        print(otp)
        forgotPass.setOTP('2615544')
        forgotPass.clickOutside()
        time.sleep(5)

        # xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert4 == alert.text)
        alert.accept()

        print('Test quen mat khau : Nhap dung ma OTP cua email khac: PASSED')

    #Test quên mật khẩu : Nhập đúng password nhận từ Email
    def test07(self):
        self.driver.get(self.baseURL)
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail(self.email)
        forgotPass.clickOutside()
        time.sleep(5)

        # Thoat Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        # Lay OTP va nhap
        otp = forgotPass.getOTP()
        print(otp)
        forgotPass.setOTP(otp)
        forgotPass.clickOutside()
        time.sleep(5)

        # xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert == alert.text)
        alert.accept()

        #Nhap mat khau de test
        forgotPass.setPasswd(forgotPass.getReturnedPasswd())
        forgotPass.clickLogin()
        time.sleep(2)  # sleep
        self.assertTrue(self.assertionText == forgotPass.getAssertText())
        forgotPass.clickLogout()
        print('Test quen mat khau : Nhap dung password nhan tu Email: PASSED')

    # Test quên mật khẩu : Nhập sai password nhận từ Email
    def test08(self):
        self.driver.get(self.baseURL)
        forgotPass = LoginPage(self.driver)
        forgotPass.clickForgortPasswd()
        forgotPass.setForgotEmail(self.email)
        forgotPass.clickOutside()
        time.sleep(5)

        # Thoat Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        alert.accept()

        # Lay OTP va nhap
        otp = forgotPass.getOTP()
        print(otp)
        forgotPass.setOTP(otp)
        forgotPass.clickOutside()
        time.sleep(5)

        # xac nhan Alert
        alert = Alert(self.driver)
        alert_text = alert.text
        self.assertTrue(self.assertionAlert == alert.text)
        alert.accept()

        # Nhap mat khau de test
        forgotPass.setPasswd('Nhom19')
        forgotPass.clickLogin()
        time.sleep(2)  # sleep

        # Switch to the alert and get its text
        alert = Alert(self.driver)
        alert_text = alert.text

        # Assert that the alert text is as expected

        self.assertTrue(self.assertionAlert5 == alert.text)

        # Close the alert
        alert.accept()

        print('Test quen mat khau : Nhap sai password nhan tu Email: PASSED')

    # Tat WebDriver
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()  # tat browser
        print('FINISHED TEST')

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports/'))
    #unittest.main()


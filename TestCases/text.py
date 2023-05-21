import unittest

from selenium import webdriver

class test(unittest.TestCase):

    driver = webdriver.Chrome(executable_path="C:\\Users\\Admin\\PycharmProjects\\Nhom19AutomationTest\\Drivers\pythchromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get('http://localhost:3000/')
        print('set up class')

    def test01(self):
        self.driver.get('https://www.youtube.com/')
        print('test01')

    def test02(self):
        self.driver.get('https://stackoverflow.com/questions/72475816/get-otp-code-from-liberomail-with-imaplib')
        print('test02')

    def test03(self):
        self.driver.get('https://finance.vietstock.vn/AAA-ctcp-nhua-an-phat-xanh.htm')
        print('test03')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print('tear down class')

if __name__ == '__main__':
    unittest.main()

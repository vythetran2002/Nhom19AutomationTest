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
    baseURL = ''
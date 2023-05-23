from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from PagesObjects.GmailPage import GetOTP
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import imaplib
import email
import re

class LoginPage():

    # locators of all elements
    txtBox_email_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[1]/input'
    txtBox_passwd_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[2]/input'
    btn_Login_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[3]/button[1]'
    btn_SignUp_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[3]/button[2]'
    btn_Google_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[3]/button[3]'
    linktxt_ForgotPasswd_Xpath = '//*[@id="root"]/div/div/div[3]/div/a'
    txt_assertion_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[2]/div[1]/div/p'
    Icon_Avatar_Xpath = '//*[@id="root"]/div/div[1]/div[2]/div[4]'
    btn_LogOut_Xpath = '//*[@id="root"]/div/div[1]/div[2]/div[4]/div/ul/li[2]'
    section_container_Xpath = '//*[@id="root"]/div'
    btn_Google_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[3]/button[3]'
    txtBox_studentEmail_ID = 'identifierId'
    btn_continute_ID = 'identifierNext'
    txtBox_studentPasswd_Xpath = '//*[@id="password"]/div[1]/div/div[1]/input'
    btn_continue2_Xpath = '//*[@id="passwordNext"]/div/button/span'
    txtBox_forgotEmail_XPath = '//*[@id="root"]/div/div/div[2]/form/div/input'
    txtBox_forgotPasswdOTP_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[2]/input'
    txtBox_nameResgister_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[1]/input'
    txtBox_emailRegister_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[2]/input'
    txtBox_passwdRegister_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[3]/input'
    btn_register_Xpath = '//*[@id="root"]/div/div/div[2]/form/div[4]/button[2]'

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.txt_username_id).send_keys(username)

    def setEmail(self,email):
        self.driver.find_element(By.XPATH,self.txtBox_email_Xpath).send_keys(email)

    def setPasswd(self, passwd):
        self.driver.find_element(By.XPATH,self.txtBox_passwd_Xpath).send_keys(passwd)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.btn_Login_Xpath).click()

    def clickSignUp(self):
        self.driver.find_element(By.XPATH,self.btn_SignUp_Xpath).click()

    def clickGoogle(self):
        self.driver.find_element(By.XPATH,self.btn_Google_Xpath).click()

    def clickForgortPasswd(self):
        self.driver.find_element(By.XPATH,self.linktxt_ForgotPasswd_Xpath).click()

    def getAssertText(self):
        return self.driver.find_element(By.XPATH,self.txt_assertion_Xpath).text

    def clickLogout(self):

        element_to_hover_over = self.driver.find_element(By.XPATH,self.Icon_Avatar_Xpath)
        element_to_click = self.driver.find_element(By.XPATH,self.btn_LogOut_Xpath)
        actions = ActionChains(self.driver)
        # Hover over the element
        actions.move_to_element(element_to_hover_over)
        actions.click(element_to_click)
        actions.perform()

    def pressEnter(self):
        self.driver.find_element(By.XPATH,self.section_container_Xpath).send_keys(Keys.ENTER)

    def clickGoogle(self,email,passwd):
        self.driver.find_element(By.XPATH,self.btn_Google_Xpath).click()
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            if "Đăng nhập - Tài khoản Google" in self.driver.title:
                break

        self.driver.find_element(By.ID,self.txtBox_studentEmail_ID).send_keys(email)
        self.driver.find_element(By.ID,self.btn_continute_ID).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.txtBox_studentPasswd_Xpath).send_keys(passwd)
        self.driver.find_element(By.XPATH,self.btn_continue2_Xpath).click()
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(5)

    def setForgotEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtBox_forgotEmail_XPath).clear()
        time.sleep(2)
        self.driver.find_element(By.XPATH,self.txtBox_forgotEmail_XPath).send_keys(email)

    def clickOutside(self):
        self.driver.find_element(By.XPATH,'//*[@id="root"]/div/div').click()

    def getOTP(self):
        otpGetter = GetOTP()
        return  otpGetter.getOTP()

    def getReturnedPasswd(self):
        newPassGetter = GetOTP()
        return newPassGetter.getReturnedPasswd()
    def setOTP(self,otp):
        self.driver.find_element(By.XPATH,self.txtBox_forgotPasswdOTP_Xpath).send_keys(otp)

    def setRegisterName(self, name):
        self.driver.find_element(By.XPATH,self.txtBox_nameResgister_Xpath).send_keys(name)

    def setRegisterEmail(self, email):
        self.driver.find_element(By.XPATH, self.txtBox_emailRegister_Xpath).send_keys(email)

    def setRegisterPasswd(self, passwd):
        self.driver.find_element(By.XPATH, self.txtBox_passwdRegister_Xpath).send_keys(passwd)

    def clickRegister(self):
        self.driver.find_element(By.XPATH, self.btn_register_Xpath).click()


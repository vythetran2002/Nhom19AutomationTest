from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from PagesObjects.LoginPage import LoginPage

class AdminPage():

    #locators of elements
    txt_assertLogin_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[2]/div[1]/div/p'
    txtBox_search_Xpath = '//*[@id="search-staff"]'
    btn_search_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div/div[1]/div'
    txt_assertTextSearch_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/table/tbody/tr/td[2]'
    btn_deletedStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div/div[2]/span[2]'
    btn_AddStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div/div[3]'
    txtBox_addNameStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[1]/input'
    txtBox_addEmailStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[2]/input'
    txtBox_addPassStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[3]/input'
    btn_addStaffFinal_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[4]/div[1]'
    btn_deleteStaff_Xpath = '//*[@id="delete-staff"]'
    btn_editStaff_Xpath = '//*[@id="edit-staff"]'
    txtBox_editNameStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[1]/input'
    txtBox_editEmailStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[2]/input'
    txtBox_editPasswdStaff_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[3]/input'
    btn_editStaffFinal_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/div[4]/div[1]'
    txt_noFound_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[3]/table/thead/h3'
    def __init__(self, driver):
        self.driver = driver

    # Test action: Add staff
    def clickAddStaff(self):
        self.driver.find_element(By.XPATH,self.btn_AddStaff_Xpath).click()
    def setNameAddStaff(self, name):
        self.driver.find_element(By.XPATH,self.txtBox_addNameStaff_Xpath).send_keys(name)
    def setEmailAddStaff(self, email):
        self.driver.find_element(By.XPATH,self.txtBox_addEmailStaff_Xpath).send_keys(email)
    def setPasswdAddStaff(self, passwd):
        self.driver.find_element(By.XPATH, self.txtBox_addPassStaff_Xpath).send_keys(passwd)

    def clickAddStaffFinal(self):
        self.driver.find_element(By.XPATH,self.btn_addStaffFinal_Xpath).click()

    # Test Action: Search Staff

    def setNameSearchStaff(self, name):
        self.driver.find_element(By.XPATH,self.txtBox_search_Xpath).send_keys(name)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.btn_search_Xpath).click()

    def getAssertSearch(self):
        return self.driver.find_element(By.XPATH, self.txt_assertTextSearch_Xpath).text

    # Test Action: Edit Staff

    def clickEditStaff(self):
        element_to_hover_over = self.driver.find_element(By.XPATH, self.btn_editStaff_Xpath)
        element_to_click = self.driver.find_element(By.XPATH, self.btn_editStaff_Xpath)
        actions = ActionChains(self.driver)
        # Hover over the element
        actions.move_to_element(element_to_hover_over)
        actions.click(element_to_click)
        actions.perform()

    def setEmailEditStaff(self, email):
        self.driver.find_element(By.XPATH, self.txtBox_editEmailStaff_Xpath).send_keys(email)

    def setNameEditStaff(self, name):
        self.driver.find_element(By.XPATH, self.txtBox_editNameStaff_Xpath).send_keys(name)

    def clickEditStaffFinal(self):
        self.driver.find_element(By.XPATH, self.btn_editStaffFinal_Xpath).click()

    # Test Action: Delete Staff
    def clickDeleteStaff(self):
        element_to_hover_over = self.driver.find_element(By.XPATH, self.btn_deleteStaff_Xpath)
        element_to_click = self.driver.find_element(By.XPATH, self.btn_deleteStaff_Xpath)
        actions = ActionChains(self.driver)
        # Hover over the element
        actions.move_to_element(element_to_hover_over)
        actions.click(element_to_click)
        actions.perform()

    def getAssertDelete(self):
        return self.driver.find_element(By.XPATH,self.txt_noFound_Xpath).text

    # Test Action: Login

    def getAssertLogin(self):
         return self.driver.find_element(By.XPATH,self.txt_assertLogin_Xpath).text

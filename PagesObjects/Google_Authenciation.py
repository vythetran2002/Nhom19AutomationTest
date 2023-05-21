from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class GoogleAuthenPage():

    #locators of elements
    btn_studentEmail_Xpath = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[2]/div'

    def __int__(self, driver):
        self.driver = driver

    def studentEmailClick(self):
        self.driver.find_element(By.XPATH,self.btn_studentEmail_Xpath).click()



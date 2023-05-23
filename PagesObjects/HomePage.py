from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

class HomePage():

    #locators of elements
    btn_live_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[1]/ul/li[1]'
    btn_inbound_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[1]/ul/li[2]'
    btn_serviceLevel_Xpath= '//*[@id="RealTimeDashBoard"]/div/div[1]/ul/li[3]'
    btn_agents_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[1]/ul/li[4]'
    btn_numbers_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[1]/ul/li[5]'
    Icon_Avatar_Xpath = '//*[@id="root"]/div/div[1]/div[2]/div[4]'
    btn_LogOut_Xpath = '//*[@id="root"]/div/div[1]/div[2]/div[4]/div/ul/li[2]'
    assertText_live_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[2]/div[1]/div/p'
    assertText_inbound_Xpath = '//*[@id="inbound"]/div/div[1]/p'
    assertText_serviceLevel_Xpath = '//*[@id="RealTimeDashBoard"]/div/div[2]/div[1]/div/p'
    assertText_agent_Xpath = '//*[@id="agents"]/div/div[1]/p'
    assertText_numbers_Xpath = '//*[@id="numbers"]/div/div[1]/p'
    assertText_logOut_Xpath = '//*[@id="root"]/div/div/div[3]/div/a'

    def __init__(self, driver):
        self.driver = driver

    def clickLive(self):
        self.driver.find_element(By.XPATH,self.btn_live_Xpath).click()

    def clickInbound(self):
        self.driver.find_element(By.XPATH,self.btn_inbound_Xpath).click()

    def clickServiceLevel(self):
        self.driver.find_element(By.XPATH, self.btn_serviceLevel_Xpath).click()

    def clickAgents(self):
        self.driver.find_element(By.XPATH, self.btn_agents_Xpath).click()

    def clickNumbers(self):
        self.driver.find_element(By.XPATH, self.btn_numbers_Xpath).click()

    def getLiveAssertText(self):
        return self.driver.find_element(By.XPATH,self.assertText_live_Xpath).text
    def getInboundAssertText(self):
        return self.driver.find_element(By.XPATH, self.assertText_inbound_Xpath).text

    def getServiceLevelAssertText(self):
        return self.driver.find_element(By.XPATH, self.assertText_serviceLevel_Xpath).text

    def getAgentsAssertText(self):
        return self.driver.find_element(By.XPATH, self.assertText_agent_Xpath).text

    def getNumbersAssertText(self):
        return self.driver.find_element(By.XPATH, self.assertText_numbers_Xpath).text

    def clickLogOut(self):

        element_to_hover_over = self.driver.find_element(By.XPATH, self.Icon_Avatar_Xpath)
        element_to_click = self.driver.find_element(By.XPATH, self.btn_LogOut_Xpath)
        actions = ActionChains(self.driver)
        # Hover over the element
        actions.move_to_element(element_to_hover_over)
        actions.click(element_to_click)
        actions.perform()

    def getLogOutAssertText(self):
        return self.driver.find_element(By.XPATH,self.assertText_logOut_Xpath).text





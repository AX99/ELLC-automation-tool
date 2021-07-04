from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Secrets import username, pw

class ellc():
    def __init__(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
    
    def login(self):
        self.driver.get('https://www.ellcchoicehomes.org.uk/HouseholdLogin')
        self.driver.implicitly_wait(3)
        cookie = self.driver.find_element_by_xpath('//*[@id="qc-cmp2-ui"]/div[2]/div/button[1]')
        cookie.click()
        
        user = self.driver.find_element_by_xpath('//*[@id="LoginReferenceField"]')
        dd = self.driver.find_element_by_xpath('//*[@id="FirstPasswordField_Day"]')
        mm = self.driver.find_element_by_xpath('//*[@id="FirstPasswordField_Month"]')
        yyyy = self.driver.find_element_by_xpath('//*[@id="FirstPasswordField_Year"]')
    
        user.send_keys(username)
        dd.send_keys(pw['dd'])
        mm.send_keys(pw['mm'])
        yyyy.send_keys(pw['yyyy'])

        sign = self.driver.find_element_by_xpath('//*[@id="LoginFormSubmitButton"]')
        sign.click()

    def bids(self):
        bids = self.driver.find_element_by_xpath('//*[@id="EligiblePropertiesCounterLinkControl"]')
        bids.click()

    

start = ellc()
start.login()
start.bids()

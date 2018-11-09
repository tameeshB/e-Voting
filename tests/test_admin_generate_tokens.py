# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os
import polls.globals as globals

class AdminGenerateTokens(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chromedriver = os.environ["webdriver_chrome"]
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
        self.driver.implicitly_wait(30)
        self.base_url = "http://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_a(self):
        driver = self.driver
        driver.get("http://localhost:8000/admin/login/?next=/admin/")
        driver.find_element_by_id("id_username").clear()
        driver.find_element_by_id("id_username").send_keys("tameeshb")
        driver.find_element_by_id("id_password").clear()
        driver.find_element_by_id("id_password").send_keys("a")
        driver.find_element_by_id("id_username").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[3]").click()
        time.sleep(1)
        driver.find_element_by_link_text("Token Dashboard").click()
        time.sleep(1)
        initialTokenCountString = driver.find_element_by_css_selector("#changelist-form > div > table > thead > tr > th > div > a").text
        time.sleep(1)
        driver.find_element_by_css_selector(".addlink").click()
        time.sleep(1)
        driver.find_element_by_id("id_tokenNo").clear()
        driver.find_element_by_id("id_tokenNo").send_keys("5")
        driver.find_element_by_name("_save").click()
        finalTokenCountString = driver.find_element_by_css_selector("#changelist-form > div > table > thead > tr > th > div > a").text
        try:
            parseNtokens = lambda inpString: int(re.match(r'([\d]+) ONE-TIME TOKENS', inpString).group(1))
        except Exception as e:
            raise "Error while matching regular expression." + e

        initialTokenCount = parseNtokens(initialTokenCountString)
        finalTokenCount = parseNtokens(finalTokenCountString)
        self.assertTrue(initialTokenCount+5 == finalTokenCount)
        
        # token = str(10000)+sha256((str(10000)+globals.secretHash).encode('utf-8')).hexdigest()[:5]
        


    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

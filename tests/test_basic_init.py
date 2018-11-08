# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os

class BasicInit(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chromedriver = os.environ["webdriver_chrome"]
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://localhost:8000/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_basic_init(self):
        driver = self.driver
        driver.delete_all_cookies()
        driver.get("http://localhost:8000/")
        driver.find_element_by_id("initTabBtn").click()
        time.sleep(5)
        driver.find_element_by_css_selector("#label_hostels_BH1").click()
        driver.find_element_by_css_selector("#label_gender_M").click()
        driver.find_element_by_id("clientKey").click()
        driver.find_element_by_id("clientKey").clear()
        driver.find_element_by_id("clientKey").send_keys("a")
        driver.find_element_by_css_selector(".primary").click()
        self.assertIn('Please log-in to proceed',self.driver.page_source)

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

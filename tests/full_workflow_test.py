# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, os

class Full(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chromedriver = os.environ["webdriver_chrome"]
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)
        self.verificationErrors = []

    def test_admin_a_init(self):
        # admin login
        self.driver.get("http://localhost:8000/admin")
        time.sleep(2)
        self.driver.find_element_by_id("id_username").click()
        self.driver.find_element_by_id("id_username").clear()
        self.driver.find_element_by_id("id_username").send_keys("tameeshb")
        self.driver.find_element_by_id("id_password").clear()
        self.driver.find_element_by_id("id_password").send_keys("a")
        self.driver.find_element_by_xpath("//*[@id=\"login-form\"]/div[3]/input").click()
        time.sleep(2)
        # Poll Control Panel
        self.driver.find_element_by_link_text("Poll Control Panel").click()
        self.driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[1]/form[1]/button").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id=\"content-main\"]/div[1]/form[4]/button").click()
        time.sleep(1)
        self.assertIn("The poll is currently in process. Results of the poll are not yet published" ,          self.driver.page_source)

    def test_b_init(self): # inherit from test_basic_init.py
        self.driver.delete_all_cookies()
        self.driver.get("http://localhost:8000/")
        self.driver.find_element_by_id("initTabBtn").click()
        time.sleep(5)
        self.driver.find_element_by_css_selector("#label_hostels_BH1").click()
        self.driver.find_element_by_css_selector("#label_gender_M").click()
        self.driver.find_element_by_id("clientKey").click()
        self.driver.find_element_by_id("clientKey").send_keys("a")
        self.driver.find_element_by_css_selector(".primary").click()
        self.assertIn('Please log-in to proceed',self.driver.page_source)

    # def test_c_login(self): # inherit from test_basic_init.py
    #     self.driver.get("http://localhost:8000/")
    #     time.sleep(5)
    #     self.driver.find_element_by_css_selector("#webmail").clear()
    #     self.driver.find_element_by_css_selector("#webmail").send_keys("biswas.cs16@iitp.ac.in")
    #     self.driver.find_element_by_id("name").clear()
    #     self.driver.find_element_by_id("name").send_keys("1601CS08")
    #     self.driver.find_element_by_id("name").clear()
    #     self.driver.find_element_by_id("name").send_keys("1601CS08")
    #     self.driver.find_element_by_id("token").clear()
    #     self.driver.find_element_by_id("token").send_keys("12962637d8")
    #     self.driver.find_element_by_id("loginTabBtn").click()
    #     self.assertIn('Vote',self.driver.page_source)

    # def test_full(self):
    #     driver = self.driver

        
    #     # init 
    #     driver.find_element_by_id("initTabBtn").click()
    #     driver.find_element_by_id("label_hostels_BH1").click()
    #     driver.find_element_by_id("label_gender_M").click()
    #     driver.find_element_by_id("clientKey").click()
    #     driver.find_element_by_id("clientKey").clear()
    #     driver.find_element_by_id("clientKey").send_keys("a")
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Client Key'])[1]/following::input[2]").click()

    #     driver.find_element_by_link_text("Polls").click()
    #     driver.find_element_by_link_text("Token Dashboard").click()
    #     driver.find_element_by_link_text("Generate More Tokens").click()
    #     driver.find_element_by_id("id_tokenNo").click()
    #     driver.find_element_by_id("id_tokenNo").clear()
    #     driver.find_element_by_id("id_tokenNo").send_keys("5")
    #     driver.find_element_by_name("_save").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Generate More Tokens'])[1]/following::td[70]").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Generate More Tokens'])[1]/following::td[70]").click()
    #     # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | xpath=(.//*[normalize-space(text()) and normalize-space(.)='Generate More Tokens'])[1]/following::td[70] | ]]
    #     driver.find_element_by_link_text("Log out").click()
    #     driver.find_element_by_id("webmail").clear()
    #     driver.find_element_by_id("webmail").send_keys("tameeshb")
    #     driver.find_element_by_id("password").clear()
    #     driver.find_element_by_id("password").send_keys("a")
    #     driver.find_element_by_id("initTabBtn").click()
    #     driver.find_element_by_id("label_hostels_BH1").click()
    #     driver.find_element_by_id("label_gender_M").click()
    #     driver.find_element_by_id("clientKey").click()
    #     driver.find_element_by_id("clientKey").clear()
    #     driver.find_element_by_id("clientKey").send_keys("a")
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Client Key'])[1]/following::input[2]").click()
    #     driver.find_element_by_id("webmail").clear()
    #     driver.find_element_by_id("webmail").send_keys("tameeshb")
    #     driver.find_element_by_id("password").clear()
    #     driver.find_element_by_id("password").send_keys("a")
    #     driver.find_element_by_id("loginTabBtn").click()
    #     driver.find_element_by_id("name").click()
    #     driver.find_element_by_id("name").clear()
    #     driver.find_element_by_id("name").send_keys("1601CS11")
    #     driver.find_element_by_id("webmail").clear()
    #     driver.find_element_by_id("webmail").send_keys("biswas.cs16")
    #     driver.find_element_by_id("password").clear()
    #     driver.find_element_by_id("password").send_keys("998099281e")
    #     driver.find_element_by_id("token").clear()
    #     driver.find_element_by_id("token").send_keys("998099281e")
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='One Time Token:'])[1]/following::input[2]").click()
    #     driver.find_element_by_id("webmail").click()
    #     driver.find_element_by_id("webmail").clear()
    #     driver.find_element_by_id("webmail").send_keys("biswas.cs16@iitp.ac.in")
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='One Time Token:'])[1]/following::input[2]").click()
    #     driver.find_element_by_link_text("Vote").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Tech Sec, 3rd Year'])[2]/following::label[1]").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Vice President'])[2]/following::label[1]").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Agenda'])[12]/following::input[1]").click()
    #     driver.find_element_by_id("webmail").clear()
    #     driver.find_element_by_id("webmail").send_keys("tameeshb")
    #     driver.find_element_by_id("password").clear()
    #     driver.find_element_by_id("password").send_keys("a")
    #     driver.find_element_by_id("verifyTabBtn").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='One Time Token:'])[2]/following::input[1]").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='One Time Token:'])[2]/following::input[1]").clear()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='One Time Token:'])[2]/following::input[1]").send_keys("998099281e")
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='One Time Token:'])[2]/following::input[2]").click()
    #     driver.find_element_by_id("webmail").clear()
    #     driver.find_element_by_id("webmail").send_keys("tameeshb")
    #     driver.find_element_by_id("password").clear()
    #     driver.find_element_by_id("password").send_keys("a")
    #     driver.find_element_by_id("error").click()
    #     driver.find_element_by_id("error").click()
    #     # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | id=error | ]]
    #     driver.find_element_by_id("id_username").clear()
    #     driver.find_element_by_id("id_username").send_keys("tameeshb")
    #     driver.find_element_by_id("id_password").clear()
    #     driver.find_element_by_id("id_password").send_keys("a")
    #     driver.find_element_by_id("login-form").submit()
    #     driver.find_element_by_id("id_password").clear()
    #     driver.find_element_by_id("id_password").send_keys("a")
    #     driver.find_element_by_link_text("Poll Control Panel").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Start Poll'])[1]/following::button[1]").click()
    #     driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Stop Poll'])[1]/following::button[1]").click()
    
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

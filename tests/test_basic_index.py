import unittest,unittest, time, re, os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
from django.test import TestCase
from django.urls import resolve
# import ..polls.globals as globals

import polls.globals as globals
import polls.views

class NewVisitorTest(TestCase):
    def setUp(self):  
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chromedriver = os.environ["webdriver_chrome"]
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)

    def tearDown(self):  
        self.driver.quit()
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, polls.views.index)

    def test_index(self):  
        
        self.driver.get('http://localhost:8000')

        self.assertIn('e-Voting portal', self.driver.title)  
        self.assertIn(globals.globals['electionName'], self.driver.title)  
        # self.fail('Finish the test!')  

    def test_login_url_resolves_to_init_on_no_init(self):
        self.driver.delete_all_cookies()
        self.driver.get('http://localhost:8000')
        self.driver.find_element_by_css_selector('.use-middle > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()
        time.sleep(5)
        self.assertIn('init',self.driver.current_url)
        # self.assertEqual(found.func, polls.views.index)

        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
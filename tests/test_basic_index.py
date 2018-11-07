import unittest,unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from django.test import TestCase
from django.urls import resolve
# import ..polls.globals as globals

import polls.globals as globals
import polls.views

class NewVisitorTest(TestCase):
    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()
    
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, polls.views.index)

    def test_index(self):  
        
        self.browser.get('http://localhost:8000')

        self.assertIn('e-Voting portal', self.browser.title)  
        self.assertIn(globals.globals['electionName'], self.browser.title)  
        # self.fail('Finish the test!')  

    def test_login_url_resolves_to_init_on_no_init(self):
        self.browser.get('http://localhost:8000')
        self.browser.find_element_by_css_selector('.use-middle > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()
        time.sleep(5)
        self.assertIn('init',self.browser.current_url)
        # self.assertEqual(found.func, polls.views.index)

        

if __name__ == '__main__':  
    unittest.main(warnings='ignore')  
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re


FIGHTERS_W_KEYWORDS = {
  'jose aldo': ['jose aldo'],
  'anderson silva': ['anderson silva'],
  'daniel cormier': ['daniel cormier', 'DC'],
  'derrick lewis': ['derrick lewis', 'swang and bang'],
  'max holloway': ['max holloway']
}


def navigate_to_rmma_new(driver_instance):
  # go to the google home page
  driver_instance.get("https://www.reddit.com/r/mma")

  sort_button = driver_instance.find_element_by_css_selector('#ListingSort--SortPicker')
  sort_button.click()
  new_button = driver_instance.find_element_by_css_selector('a.s1vspxim-2:nth-child(2)')
  # new_button = driver_instance.find_element_by_css_selector('a[href="/r/mma/new/"]')
  new_button.click()

  print(driver_instance.title)


def scroll_to_bottom(driver_instance):
  driver_instance.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  time.sleep(5)


def scroll_to_top(driver_instance):
  driver_instance.execute_script("window.scrollTo(0, 0);")
  time.sleep(5)



class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.reddit.com/r/mma")
        driver.find_element_by_id("ListingSort--SortPicker").click()
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='hot'])[2]/following::span[1]").click()
    
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
  # unittest.main()

  # Create a new instance of the Firefox driver
  driver = webdriver.Firefox()

  navigate_to_rmma_new(driver)

  scroll_to_bottom(driver)
  # WebDriverWait(driver, 30).until(EC.staleness_of(html_elem))

  fighter_elements = driver.find_elements_by_xpath("//*[contains(text(), \"{}\")]".format("Ariel's"))

  for element in fighter_elements:
    if element.text:
      print(element.text)

  # driver.quit()
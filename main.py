from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.by import By
import time


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


if __name__ == "__main__":
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
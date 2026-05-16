from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')
sleep(2)

# By ID
element = driver.find_element(By.ID, 'twotabsearchtextbox')

# CSS selector, using id
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# CSS selector, class .
driver.find_element(By.CSS_SELECTOR, '.nav-sprite-v1.nav-progressive-attribute.hamburger')
driver.find_element(By.CSS_SELECTOR, '.hamburger.nav-sprite-v1.nav-progressive-attribute')
driver.find_element(By.CSS_SELECTOR, 'div.hamburger.nav-sprite-v1.nav-progressive-attribute')
# CSS selector, tag + id + 3 classes
driver.find_element(By.CSS_SELECTOR, 'div#navbar.hamburger.nav-sprite-v1.nav-progressive-attribute')

# CSS selector, attributes
driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
# CSS selector, 2 attributes
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][aria-label='Search Amazon']")
# CSS selector, tag + 2 attributes
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][aria-label='Search Amazon']")
# CSS selector, tag + class + 2 attributes
driver.find_element(By.CSS_SELECTOR, "input.nav-input[placeholder='Search Amazon']")

# CSS selector, contains *=
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search']")
driver.find_element(By.CSS_SELECTOR, "input.nav-input[placeholder*='Search']")
driver.find_element(By.CSS_SELECTOR, "h1[class*='Heading']")
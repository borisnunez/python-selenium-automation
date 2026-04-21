from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://stackoverflow.com/users/signup')

#Homework Locators

#Create your account Locator
driver.find_element(By.XPATH, "//h1[text()='Create your account']")

#By Clicking "Sign up", you agree to our terms Locator
driver.find_element(By.CSS_SELECTOR, 'div[class*="js-terms"]')

#Email Locator
driver.find_element(By.CSS_SELECTOR, 'input[id="email"]')

#Password Locator
driver.find_element(By.CSS_SELECTOR, 'input[id="password"]')

#Show password Locator
driver.find_element(By.CSS_SELECTOR, 'svg[class*="js-show-password"]')

#Sign Up Locator
driver.find_element(By.CSS_SELECTOR, 'button[id="submit-button"]')

#Google sign up Locator
driver.find_element(By.CSS_SELECTOR, 'button[data-provider="google"]')

#Github sign up Locator
driver.find_element(By.CSS_SELECTOR, 'button[data-provider="github"]')

#Get Stack Overflow Internal free for up to 50 users Locator
driver.find_element(By.XPATH, "//a[text()='Get Stack Overflow Internal free for up to 50 users']")



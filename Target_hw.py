from selenium import webdriver
from selenium.webdriver import Keys
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
driver.get('https://www.target.com/')
sleep(3)

#click the account button
driver.find_element(By.XPATH, "//span[@class='sc-1a162949-3 iuQwR display-name h-margin-r-x3']").click()
sleep(3)
driver.find_element(By.XPATH, '//button[@data-test="accountNav-signIn"]').click()
sleep(3)

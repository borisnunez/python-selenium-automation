from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.implicitly_wait(5)  # applied to all find element(s) ==> check for E e/100ms
driver.wait = WebDriverWait(driver, timeout=10) # applied to wait.until(), waits for condition to be met e/0.5 sec

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Table')

# wait for 4 sec
# sleep(4)
search_btn = (By.NAME, 'btnK')
driver.wait.until(EC.element_to_be_clickable(search_btn), message='Search button not clickable').click()
# also driver.wait.until_not is used                        # insert message to see error clearly
# click search button
#driver.find_element(By.NAME, 'btnK').click()

# verify search results
driver.wait.until(EC.url_contains('Table'), message=f"Expected query not in {driver.current_url}")
#assert 'table'.lower() in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()

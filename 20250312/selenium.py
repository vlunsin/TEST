from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# need chrome driver in same folder as python script
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# to use the driver on google.com
driver.get("https://google.com")

# need to take care of timimn
# search with By the first element 
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
#it will type in search of google
# clear an element
input_element.clear()
# plus keyboard ENTER
input_element.send_keys("example of search" + Keys.ENTER)

# waiting time for webdriver
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located(By.CLASS_NAME, "gLFyf")
)
# lot of issues, because of bots

# to find and click on a link
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Link to find")
link.click

# to make a timer of 10 seconds
time.sleep(10)

#Example of cookie site
# inspect the big cookie, get the id
# error with selection of language
# use XPATH to and search with By.XPATH

# to quit the driver
driver.quit()
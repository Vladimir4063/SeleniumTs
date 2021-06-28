import time
from selenium import webdriver

driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get('https://www.google.com')
time.sleep(3)

search_box = driver.find_element_by_name("q")
search_box.send_keys("Vladimir")
time.sleep(2)

driver.quit()

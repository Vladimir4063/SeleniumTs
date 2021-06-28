from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select #interactuamos con los select/value

driver = webdriver.Chrome('driver/chromedriver.exe')
driver.get('https://www.timeanddate.com/')
time.sleep(5)
 
#driver.find_element_by_name("country").click()

countryDropDown = Select(driver.find_element_by_name("country")) #no damos click, pero no posicionamos
countryDropDown.select_by_index(5) #seleccionamos por index
time.sleep(2)
countryDropDown.select_by_value("27") #por atributo value del html
time.sleep(2)
countryDropDown.select_by_visible_text("India") #segun el texto
time.sleep(3)
driver.quit()

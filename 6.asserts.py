from os import link
from selenium import webdriver
import time

driver = webdriver.Chrome('driver/chromedriver.exe')  # ruta del driver

# llamamos al navegador
driver.get('https://blazedemo.com/')
time.sleep(3)

#user_box = driver.find_element_by_name('username')  # name=html
#pass_box = driver.find_element_by_name('password')
#submit_button = driver.find_element_by_class_name('btn')  # class

#user_box.send_keys('vladimirgutierrez4063@gmail.com')
#pass_box.send_keys('Contravlady97')
#submit_button.click()
#time.sleep(5)

link_registration_form = driver.find_element_by_link_text('destination of the week! The Beach!')
assert link_registration_form.text == 'destination of the week! The Beach!' #asserts: condicional
#assert link_registration_form.text =='registration form' 
assert link_registration_form.tag_name == "a"

print("Process finished successfully")

time.sleep(3)

driver.quit()

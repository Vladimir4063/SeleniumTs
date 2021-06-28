from selenium import webdriver
import time

driver = webdriver.Chrome('driver/chromedriver.exe')  # ruta del driver

# llamamos al navegador
driver.get('https://cursos.polotic.misiones.gob.ar/login.php')
time.sleep(5)

#user_box = driver.find_element_by_name('username')  # name=html
user_box = driver.find_element_by_xpath('//*[@id="username"]') #puedes elegir usar el Xpath completo o no.
#user_box = driver.find_element_by_css_selector('')
#pass_box = driver.find_element_by_name('password')
pass_box = driver.find_element_by_xpath('//*[@id="password"]')

submit_button = driver.find_element_by_class_name('btn')  # class

user_box.send_keys('vladimirgutierrez4063@gmail.com')
pass_box.send_keys('Contravlady97')
#submit_button.click()
time.sleep(5)

driver.quit()
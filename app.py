from selenium import webdriver
import time

driver = webdriver.Chrome('driver/chromedriver.exe') #ruta del driver

# llamamos al navegador
driver.get('https://cursos.polotic.misiones.gob.ar/login.php')
time.sleep(5)

user_box = driver.find_element_by_name('username')
pass_box = driver.find_element_by_name('password')
submit_button = driver.find_element_by_class_name('btn')

user_box.send_keys('vladimirgutierrez4063@gmail.com')
pass_box.send_keys('Contravlady97')
submit_button.click()
time.sleep(5)

driver.quit()


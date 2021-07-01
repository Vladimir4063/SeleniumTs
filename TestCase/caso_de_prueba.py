from selenium import webdriver
import unittest
import time

class Items(unittest.TestCase): #indicamos que sera unitest
    
    def setUp(self): #funcion que solo abre el nav
        self.driver = webdriver.Chrome('driver/chromedriver.exe')
        self.driver.get('https://www.mercadolibre.com.ar')

    def test_do_nothing(self): #Primer caso de solo abrir y cerrar
        time.sleep(4)
        self.driver.quit()

    def test_view_item_page(self):
        time.sleep(3)
        self.driver.find_element_by_class_name('nav-search-input').send_keys('pc')
        self.driver.find_element_by_class_name('nav-icon-search').click()
        time.sleep(3)
        #self.driver.find_element_by_xpath('//*[@id="root-app"]/div/div[1]/section/ol[1]/li[2]/div/div/div[1]/a/div/div/div[2]/div/div[1]/img').click()
        self.driver.find_elements_by_class_name('ui-search-item__title ui-search-item__group__element').click()
        #self.driver.find_elements_by_link_text('Pc Armada Slim Intel Amd Dual Core Hd 1tb 8gb Ram Lol Hdmi').click()
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

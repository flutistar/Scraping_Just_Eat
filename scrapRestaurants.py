#Search restaurants list with Postcodes

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
class scrapRestaurants():
    def loaddriver(postcodes):
        restaurantUrls = []
        baseUrl = "https://www.just-eat.co.uk/"
        currentPath = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver.exe'
        driver = webdriver.Chrome(executable_path= currentPath)
        i = 0
        for pcode in postcodes:
            i+=1
            if i>10:
                break    
            driver.get(baseUrl)
            search_box = driver.find_element(By.XPATH, "//input[@data-test-id='address-box-input']")
            time.sleep(0.5)
            search_box.clear()
            search_box.send_keys(pcode)
            print(pcode)
            search_box.submit()
            lis = driver.find_elements_by_xpath("//div[@data-test-id='openrestaurants']/section[@data-test-id='restaurant']/a")
            time.sleep(2)            
            for item in lis:
                restaurantUrls.append(item.get_attribute('href'))
        driver.quit()
        return restaurantUrls

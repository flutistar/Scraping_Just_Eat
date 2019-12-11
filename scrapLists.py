from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import xlsxwriter 

class scrapLists():
    def getList(urls):
        currentPath = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver.exe'
        driver = webdriver.Chrome(executable_path= currentPath)
        workbook = xlsxwriter.Workbook('Restaurants.xlsx') 
        worksheet = workbook.add_worksheet("rstDetails")
        row_count = 0
        #Set Sheet Colum Width
        worksheet.set_column('A:A', 40)
        worksheet.set_column('B:B', 20)
        worksheet.set_column('C:C', 40)
        #Set Sheet Colum Header
        worksheet.write(row_count, 0, 'NAME')
        worksheet.write(row_count, 1, "FOOD TYPE")
        worksheet.write(row_count, 2, "ADDRESS")
        for url in urls:
            driver.get(url)
            details = driver.find_element_by_xpath("//div[@class='restaurantOverview o-card u-negativeSpace--top']/div[2]")
            rstName= details.find_element_by_xpath("//h1[@class='name']").text
            rstFood = details.find_element_by_xpath("//p[@class='cuisines']/span[1]").text + ', ' + details.find_element_by_xpath("//p[@class='cuisines']/span[2]").text
            rstAddress = details.find_element_by_xpath("//p[@class='address']/span[1]").text + ', ' + details.find_element_by_xpath("//p[@class='address']/span[2]").text
            row_count += 1
            worksheet.write(row_count, 0, rstName)
            worksheet.write(row_count, 1, rstFood)
            worksheet.write(row_count, 2, rstAddress)
        workbook.close()
        driver.quit()
        # return rstName, rstFood, rstAddress

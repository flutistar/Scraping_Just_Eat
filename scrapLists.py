from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import xlsxwriter 


def getList(urls):
    currentPath = os.path.dirname(os.path.realpath(__file__)) + '/chromedriver.exe'
    driver = webdriver.Chrome(executable_path= currentPath)
    workbook = xlsxwriter.Workbook('Restaurants.xlsx') 
    worksheet = workbook.add_worksheet("rstDetails")
    row_count = 0
    #Set Sheet Colum Width
    worksheet.set_column('A:A', 40)
    worksheet.set_column('B:B', 20)
    worksheet.set_column('C:C', 60)
    #Set Sheet Colum Header
    worksheet.write(row_count, 0, 'NAME')
    worksheet.write(row_count, 1, "FOOD TYPE")
    worksheet.write(row_count, 2, "ADDRESS")
    for url in urls:
        rstName = ''
        rstFood = ''
        rstAddress = ''
        if url[0:5] == 'off: ':
            rstName = '* '
            url = url[5:]
        try:
            driver.get(url)
            details = driver.find_element_by_xpath("//div[@class='restaurantOverview o-card u-negativeSpace--top']/div[2]")
            rstName += details.find_element_by_xpath("//h1[@class='name']").text
            Foods = details.find_elements_by_xpath("//p[@class='cuisines']/span")
            if(len(Foods) > 1):
                rstFood = details.find_element_by_xpath("//p[@class='cuisines']/span[1]").text + ', ' + details.find_element_by_xpath("//p[@class='cuisines']/span[2]").text
            else:
                rstFood = details.find_element_by_xpath("//p[@class='cuisines']/span[1]").text
            rstAddress = details.find_element_by_xpath("//p[@class='address']/span[1]").text + ', ' + details.find_element_by_xpath("//p[@class='address']/span[2]").text + ', ' + details.find_element_by_xpath("//p[@class='address']/span[3]").text
        except Exception as ex:
            pass
            print("passed: ", ex, "    ", url)
        row_count += 1
        worksheet.write(row_count, 0, rstName)
        worksheet.write(row_count, 1, rstFood)
        worksheet.write(row_count, 2, rstAddress)
        print(row_count, "scraped", url, "   ", rstName)
    workbook.close()
    driver.quit()
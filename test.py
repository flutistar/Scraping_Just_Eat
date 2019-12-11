# import xlsxwriter module 
import xlsxwriter 

def insertintoSheet(Urls):
    workbook = xlsxwriter.Workbook('Restaurants.xlsx') 
    worksheet = workbook.add_worksheet("rstURLs")
    row_count = 0
    print(len(Urls))
    for url in Urls:
        row_count += 1
        worksheet.write(row_count, 0, url)
        print(url)
    print(row_count)  
    workbook.close()

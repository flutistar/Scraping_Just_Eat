# import xlsxwriter module 
import xlsxwriter 

def insertintoSheet(Urls):
    workbook = xlsxwriter.Workbook('URLs.xlsx') 
    worksheet = workbook.add_worksheet("rstURLs")
    row_count = 0
    print("Total URLs : ", len(Urls))
    for url in Urls:
        row_count += 1
        worksheet.write(row_count, 0, url)
    
    workbook.close()

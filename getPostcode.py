import xlrd 


class getPostcode():
    def importXlsx():
        xlsPath = ("Postcode districts-modified.xlsx")  
        wb = xlrd.open_workbook(xlsPath) 
        sheet = wb.sheet_by_index(0) 
        num_cols = sheet.nrows - 1
        postcodes = []
        for i in range(1,num_cols):
            postcodes.append(sheet.cell_value(i, 0))
        postcodes.extend('Postcode')
        return postcodes
    def checkDuplicate(inputList):
        results = [] 
        for item in inputList: 
            if item not in results: 
                results.append(item)
        return results 

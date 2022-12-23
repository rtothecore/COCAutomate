import openpyxl

xlsPath = r'C:/Users/user/Desktop/AutomateProject/Order_Folder/해지시공-대상리스트.xlsx'
wb = openpyxl.load_workbook(xlsPath)
sheet1 = wb.active
sheet1.append(['test', 2, 3, 4, 5])
wb.save(xlsPath)
from easyocr import Reader
import cv2
import os
import shutil
import time
import excel_processor
import property_manager

##################################### Using EasyOCR #########################################################
'''
path = r'C:/Users/user/Desktop/AutomateProject/Order_Folder/NEW/Scan_20221214_143310_002.jpg'
image = cv2.imread(path)

langs = ['ko', 'en']
 
print("[INFO] OCR'ing input image...")
reader = Reader(lang_list=langs, gpu=True)
results = reader.readtext(image)
results

simple_results = reader.readtext(image, detail = 0)
simple_results
'''


def runEasyOCR(path):
    time.sleep(0.1)     # delay
    image = cv2.imread(path)
    langs = ['ko', 'en']
 
    print("[INFO] OCR'ing input image...")
    reader = Reader(lang_list=langs, gpu=True)
    results = reader.readtext(image)
    # results = [[], [], [], ['','08-1234-5678','']]    # 빠른 테스트를 위한 더미코드

    # OCR 처리후 OCR폴더로 이미지파일을 이동
    Dname = os.path.dirname(path)
    Fname, Extension = os.path.splitext(os.path.basename(path))
    old_file = os.path.join(Dname, Fname + Extension)
    # new_file = os.path.join(Dname.replace('NEW', 'OCR'), Fname + Extension)   
    movePath = property_manager.glPropMovePath
    new_file = os.path.join(movePath, Fname + Extension)
    time.sleep(0.1)     # delay
    shutil.move(old_file, new_file)

    return results

def writeTXT(contents, txtPath):
    f = open(txtPath, 'w')
    # f.write(contents[3][1])
    f.write("This is test contents")
    f.close()

def writeExcel(contents, excelPath):
    excel_processor.writeToExcel(contents, excelPath)

def runEasyOCR_MK1(filePath):    
    results = runEasyOCR(filePath)
    # writeExcel(results, r"C:/Users/user/Desktop/AutomateProject/Order_Folder/new.xlsx")
    excelPath = property_manager.glPropExcelPath
    writeExcel(results, excelPath)
    # writeTXT(results, "C:/Users/user/Desktop/AutomateProject/Order_Folder/OCR/" + results[3][1] +".txt")
    

# test code
# runEasyOCR_MK1(r'C:/Users/user/Desktop/AutomateProject/Order_Folder/NEW/ocr_test.jpg')
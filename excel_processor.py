import pandas as pd
import datetime
import ocr_data_extractor
import os.path
import re


def writeToExcel(data, excelPath):

    now = datetime.datetime.now()
    today = now.strftime('%Y-%m-%d')
    customNo = ocr_data_extractor.extractData(data, ocr_data_extractor.tolerance_custom_no)
    customNo = re.sub(r"[^0-9]", "", customNo)  # 고객번호에서 숫자만 남기기
    customName = ocr_data_extractor.extractData(data, ocr_data_extractor.tolerance_custom_name)

    raw_data = {'시공서발행일' : [today],
                '고객번호' : [customNo],
                '고객명' : [customName]} 

    # 3개의 key : value를 가진 딕셔너리
    '''
    raw_data = {'시공서발행일' : ['2022-12-16', '2022-12-16', '2022-12-16', '2022-12-16'],
                '고객번호' : ['08-1234-5678', '08-1234-5679', '08-1234-5680', '08-1234-5681'],
                '고객명' : ['홍길동', '임꺽정', '김철수', '김영희']} 
    '''

    if os.path.exists(excelPath):
        print('Excel file exists!')
        df_original = pd.read_excel(excelPath)      # 기존의 엑셀파일이 존재하면 해당 파일을 읽음
        df = pd.DataFrame(raw_data)                 # 위 딕셔너리를 받아서 그대로 dataframe으로 생성        
        df_result = pd.concat([df_original, df])    # df_original 과 df를 연결
        df_result.to_excel(excelPath, index=False)
    else:
        print('No file exists!')
        df = pd.DataFrame(raw_data)
        df.to_excel(excelPath, index=False)         # DF를 엑셀파일로 저장
    
    # df.to_excel('C:/Users/user/Desktop/AutomateProject/Order_Folder/new.xlsx')
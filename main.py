import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import property_manager

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("ui/automate.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        # 버튼 시그널 코드
        self.BTN_OCR_PATH.clicked.connect(self.btnOcrPathFunc)
        self.BTN_MOVE_PATH.clicked.connect(self.btnMovePathFunc)
        self.BTN_EXCEL_PATH.clicked.connect(self.btnExcelPathFunc)
        self.BTN_RUN.clicked.connect(self.btnRunFunc)

        # config.ini 파일의 설정값을 읽어서 위젯에 설정
        property_manager.readProperties()
        self.LE_OCR_PATH.setText(property_manager.glPropWatchPath)
        self.LE_MOVE_PATH.setText(property_manager.glPropMovePath)
        self.LE_EXCEL_PATH.setText(property_manager.glPropExcelPath)

    def btnOcrPathFunc(self) :
        print("btn_ocr_path clicked!")
        dirName = QFileDialog.getExistingDirectory(self)
        self.LE_OCR_PATH.setText(dirName)
        property_manager.writeProperties('PATH', 'watchPath', dirName)      # config.ini 파일에 설정값을 쓰기
    
    def btnMovePathFunc(self) :
        print("btn_move_path clicked!")
        dirName = QFileDialog.getExistingDirectory(self)
        self.LE_MOVE_PATH.setText(dirName)
        property_manager.writeProperties('PATH', 'movePath', dirName)      # config.ini 파일에 설정값을 쓰기
        if self.LE_EXCEL_PATH.text() == '' :        # 엑셀파일 경로를 설정하지 않은 상태라면 자동으로 엑셀파일 경로를 입력해준다.
            self.LE_EXCEL_PATH.setText(dirName + '/new.xlsx')
            property_manager.writeProperties('PATH', 'excelPath', dirName + '/new.xlsx')      # config.ini 파일에 설정값을 쓰기

    def btnExcelPathFunc(self) :
        print("btn_excel_path clicked!")
        fName = QFileDialog.getOpenFileName(self, '', '', 'Excel 파일(*.xlsx *xls)')
        self.LE_EXCEL_PATH.setText(fName[0])
        property_manager.writeProperties('PATH', 'excelPath', fName[0])      # config.ini 파일에 설정값을 쓰기
    
    def btnRunFunc(self) :
        if self.LE_OCR_PATH.text() == '' :
            print("작업할 폴더를 설정하세요!")
            QMessageBox.warning(self, '작업폴더 설정', '작업할 폴더를 설정하세요!')
            return
        elif self.LE_MOVE_PATH.text() == '' :
            print("작업 후 이동할 폴더를 설정하세요!")
            QMessageBox.warning(self, '이동폴더 설정', '작업 후 이동할 폴더를 설정하세요!')
            return
        elif self.LE_EXCEL_PATH.text() == '' :
            print("자동입력할 엑셀파일을 설정하세요!")
            QMessageBox.warning(self, '엑셀파일 설정', '자동입력할 엑셀파일을 설정하세요!')
            return
        print("btn_run clicked!")

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
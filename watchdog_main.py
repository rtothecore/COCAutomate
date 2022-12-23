import time
import os
import ocr_processor
import property_manager

try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except ModuleNotFoundError as e:
    print (e)
    os.system("pip install watchdog")

# ------------------------------------------------
class Handler(FileSystemEventHandler):
    
    def on_created(self, event): # 파일 생성시
        print (f'event type : {event.event_type}\n'

               f'event src_path : {event.src_path}')
        if event.is_directory:
            print ("디렉토리 생성")
        else: # not event.is_directory
            Fname, Extension = os.path.splitext(os.path.basename(event.src_path))

            if Extension == '.jpg':
                print (".jpg 사진 파일 입니다.")
                ocr_processor.runEasyOCR_MK1(event.src_path)
                # os.remove(Fname + Extension)
            elif Extension == '.pdf':
                print (".pdf 문서 파일 입니다.")
                # os.remove(Fname + Extension)   # _파일 삭제 event 발생            
    '''
    def on_modified(self, event):
        print (f'event type : {event.event_type}\n'

               f'event src_path : {event.src_path}')
        if event.is_directory:
            print ("디렉토리 생성")
        else: # not event.is_directory
            Fname, Extension = os.path.splitext(os.path.basename(event.src_path))

            if Extension == '.jpg':
                print (".jpg 사진 파일 입니다.")
                easy_ocr_mk1.runEasyOCR_MK1(event.src_path)
                # os.remove(Fname + Extension)
            elif Extension == '.pdf':
                print (".pdf 문서 파일 입니다.")
    '''
    def on_deleted(self, event):
        print ("삭제 이벤트 발생")

    def on_moved(self, event): # 파일 이동시
        print (f'event type : {event.event_type}\n')

class Watcher:
    # 생성자
    def __init__(self, path):
        print ("감시 중 ...")
        self.event_handler = None      # Handler
        self.observer = Observer()     # Observer 객체 생성
        self.target_directory = path   # 감시대상 경로
        self.currentDirectorySetting() # instance method 호출 func(1)

    # func (1) 현재 작업 디렉토리
    def currentDirectorySetting(self):
        print ("====================================")
        print ("현재 작업 디렉토리:  ", end=" ")
        os.chdir(self.target_directory)
        print ("{cwd}".format(cwd = os.getcwd()))
        print ("====================================")

    # func (2)
    def run(self):
        self.event_handler = Handler() # 이벤트 핸들러 객체 생성
        self.observer.schedule(
            self.event_handler,
            self.target_directory,
            recursive=False
        )

        self.observer.start() # 감시 시작
        try:
            while True: # 무한 루프
                time.sleep(3) # 3초 마다 대상 디렉토리 감시
        except KeyboardInterrupt as e: # 사용자에 의해 "ctrl + z" 발생시
            print ("감시 중지...")
            self.observer.stop() # 감시 중단

# myWatcher = Watcher(r"C:/Users/user/Desktop/AutomateProject/Order_Folder/NEW")
property_manager.readProperties()       # 설정파일 읽기
watchPath = property_manager.glPropWatchPath
myWatcher = Watcher(watchPath)
myWatcher.run()
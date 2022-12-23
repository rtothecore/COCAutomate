import configparser as parser

# 전역변수
glProperties = ''
glPropWatchPath = ''
glPropMovePath = ''
glPropExcelPath = ''

def readProperties() :                  # ConfigParser로 설정정보 읽기
    global glProperties                 # 전역변수 사용
    glProperties = parser.ConfigParser()
    glProperties.read('./config.ini')

    global glPropWatchPath, glPropMovePath, glPropExcelPath     # 전역변수 사용
    glPropWatchPath = glProperties['PATH']['watchPath']
    glPropMovePath = glProperties['PATH']['movePath']
    glPropExcelPath = glProperties['PATH']['excelPath']

def writeProperties(section, key, value) :       # ConfigParser로 설정정보 쓰기
    global glProperties
    glProperties[section][key] = value

    with open('./config.ini', 'w') as configfile:
        glProperties.write(configfile)
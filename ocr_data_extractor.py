import rect

######################################################################################################
offset_bounding_box = 30     # 글자 바운딩 박스 허용범위 오프셋

tolerance_custom_name = rect.Rect() 
tolerance_custom_name.top_left = rect.Point(1087 - offset_bounding_box, 457 - offset_bounding_box)
tolerance_custom_name.bottom_right = rect.Point(1301 + offset_bounding_box, 561 + offset_bounding_box)

tolerance_custom_no = rect.Rect() 
tolerance_custom_no.top_left = rect.Point(2452 - offset_bounding_box, 474 - offset_bounding_box)
tolerance_custom_no.bottom_right = rect.Point(2994 + offset_bounding_box, 577 + offset_bounding_box)
######################################################################################################

# data가 targetData 영역안에 있는지 체크하여 안에 있다면 해당 데이터를 리턴
def extractData(data, targetData):
    resultData = 'no data'
    for i in range(len(data)):
        tempBoundingBox = rect.Rect()
        tempBoundingBox.top_left = rect.Point(data[i][0][0][0], data[i][0][0][1])       # top_left x, y
        tempBoundingBox.bottom_right = rect.Point(data[i][0][2][0], data[i][0][2][1])   # bottom_right x, y
        if rect.intersects(targetData, tempBoundingBox):
            resultData = data[i][1]
            break
    return resultData

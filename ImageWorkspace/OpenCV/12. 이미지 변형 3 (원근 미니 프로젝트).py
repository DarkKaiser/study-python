import cv2
import numpy as np

COLOR = (255, 0, 255)
THICKNESS = 3
drawing = False # 선을 그릴지 여부

point_list = []

img = cv2.imread("poker.jpg")

def mouse_handler(event, x, y, flags, param):
    global drawing
    
    dst_img = img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        point_list.append((x, y))
        
    if drawing == True:
        prev_point = None
        for point in point_list:
            cv2.circle(dst_img, point, 15, COLOR, cv2.FILLED)
            if prev_point != None:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point
    
        next_point = (x, y)
        if len(point_list) == 4:
            show_result()
            next_point = point_list[0]
            
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
    
    cv2.imshow("image", dst_img)

def show_result():
    width, height = 530, 710    # 가로 크기 530, 세로 크기 710으로 결과물 출력

    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)    # output 4개 지점

    matrix = cv2.getPerspectiveTransform(src, dst)              # Matrix 얻어옴
    result = cv2.warpPerspective(img, matrix, (width, height))  # matrix대로 변환을 함
    
    cv2.imshow("result", result)

# image란 이름의 윈도우를 먼저 만들어두는 것, 여기에 마우스 이벤트를 처리하기 위한 핸들러 적용
cv2.namedWindow("image")
cv2.setMouseCallback("image", mouse_handler)

cv2.imshow("image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

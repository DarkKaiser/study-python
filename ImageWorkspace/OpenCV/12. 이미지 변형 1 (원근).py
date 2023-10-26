import cv2
import numpy as np

#
# 사다리꼴 이미지 펼치기
# 

img = cv2.imread("ImageWorkspace/OpenCV/newspaper.jpg")

width, height = 640, 240    # 가로 크기 640, 세로 크기 240으로 결과물 출력

src = np.array([[255, 176], [504, 172], [561, 292], [227, 297]], dtype=np.float32)      # input 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)    # output 4개 지점

matrix = cv2.getPerspectiveTransform(src, dst)              # Matrix 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height))  # matrix대로 변환을 함

cv2.imshow("image", img)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

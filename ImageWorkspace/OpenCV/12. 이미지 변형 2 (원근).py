import cv2
import numpy as np

#
# 회전된 이미지 올바로 세우기
# 

img = cv2.imread("poker.jpg")

width, height = 530, 710    # 가로 크기 530, 세로 크기 710으로 결과물 출력

src = np.array([[702, 143], [1133, 414], [726, 1007], [276, 700]], dtype=np.float32)      # input 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0, height]], dtype=np.float32)    # output 4개 지점

matrix = cv2.getPerspectiveTransform(src, dst)              # Matrix 얻어옴
result = cv2.warpPerspective(img, matrix, (width, height))  # matrix대로 변환을 함

cv2.imshow("image", img)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# 팽창
# 이미지를 확장하여 작은 구멍을 채움
# 흰색 영역의 외곽 픽셀 주변에 흰색을 추가

kernel = np.ones((3, 3), dtype=np.uint8)

img = cv2.imread("dilate.png", cv2.IMREAD_GRAYSCALE)
dilate1 = cv2.dilate(img, kernel=kernel, iterations=1)  # iterations : 반복횟수
dilate2 = cv2.dilate(img, kernel=kernel, iterations=2)
dilate3 = cv2.dilate(img, kernel=kernel, iterations=3)

cv2.imshow("image", img)
cv2.imshow("dilate1", dilate1)
cv2.imshow("dilate2", dilate2)
cv2.imshow("dilate3", dilate3)

cv2.waitKey(0)
cv2.destroyAllWindows()

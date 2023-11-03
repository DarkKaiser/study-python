import cv2
import numpy as np

# 닫힘 : 팽창 후 침식, 구멍을 메운 후 다시 깍음

kernel = np.ones((3, 3), dtype=np.uint8)

img = cv2.imread("ImageWorkspace/OpenCV/dilate.png", cv2.IMREAD_GRAYSCALE)
dilate = cv2.dilate(img, kernel=kernel, iterations=2)
erode = cv2.erode(dilate, kernel=kernel, iterations=2)

cv2.imshow("image", img)
cv2.imshow("dilate", dilate)
cv2.imshow("erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# 열림 : 침식 후 팽창, 깍아서 노이즈 제거 후 다시 살 찌움

kernel = np.ones((3, 3), dtype=np.uint8)

img = cv2.imread("erode.jpg", cv2.IMREAD_GRAYSCALE)
erode = cv2.erode(img, kernel=kernel, iterations=2)
dilate = cv2.dilate(erode, kernel=kernel, iterations=2)

cv2.imshow("image", img)
cv2.imshow("erode", erode)
cv2.imshow("dilate", dilate)

cv2.waitKey(0)
cv2.destroyAllWindows()

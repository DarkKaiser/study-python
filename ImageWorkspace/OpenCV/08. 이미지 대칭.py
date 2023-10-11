import cv2

img = cv2.imread("img.jpg")

# 좌우대칭
flip_horizontal = cv2.flip(img, flipCode=1)  # flipCode > 0 : 좌우대칭

# 상하대칭
flip_vertical = cv2.flip(img, flipCode=0)  # flipCode == 0 : 상하대칭

# 상하좌우대칭
flip_both = cv2.flip(img, flipCode=-1)  # flipCode < 0 : 상하좌우대칭

cv2.imshow("image", img)
cv2.imshow("flip_horizontal", flip_horizontal)
cv2.imshow("flip_vertical", flip_vertical)
cv2.imshow("flip_both", flip_both)

cv2.waitKey(0)
cv2.destroyAllWindows()

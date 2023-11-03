import cv2

img = cv2.imread("ImageWorkspace/OpenCV/img.jpg")

# 시계 방향으로 90도 회전
roate_90 = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("image", img)
cv2.imshow("roate_90", roate_90)

cv2.waitKey(0)
cv2.destroyAllWindows()

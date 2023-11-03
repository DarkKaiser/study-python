import cv2

img = cv2.imread("ImageWorkspace/OpenCV/img.jpg")

# 불러온 이미지를 흑백으로 변경
dst = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("image", img)
cv2.imshow("COLOR_BGR2GRAY", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

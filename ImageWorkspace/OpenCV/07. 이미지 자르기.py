import cv2

img = cv2.imread("ImageWorkspace/OpenCV/img.jpg")

crop = img[100:200, 200:400]

# 영역을 잘라서 기존 윈도우에 출력
img[100:200, 400:600] = crop

cv2.imshow("image", img)
cv2.imshow("crop image", crop)

cv2.waitKey(0)
cv2.destroyAllWindows()

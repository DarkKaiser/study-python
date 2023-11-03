import cv2

# 오츠 알고리즘
# Bimodal Image에 사용하기 적합(최적의 임계치를 자동으로 발견)

img = cv2.imread("ImageWorkspace/OpenCV/book.jpg", cv2.IMREAD_GRAYSCALE)

ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print("otsu threshold", ret)

cv2.imshow("image", img)
cv2.imshow("binary", binary)
cv2.imshow("otsu", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()

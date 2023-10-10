import cv2

img = cv2.imread("img.jpg")
dst1 = cv2.resize(img, (400, 500))              # Width, Height 크기 고정
dst2 = cv2.resize(img, None, fx=0.5, fy=0.5)    # x, y 비율 정의(0.5배로 축소)
# 보간법을 활용한 x, y 비율 정의(0.5배로 축소)
dst3 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("image", img)
cv2.imshow("resize", dst1)
cv2.imshow("scale", dst2)
cv2.imshow("scale(interpolation)", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# 보간법
# cv2.INTER_AREA : 크기 줄일 때 사용
# cv2.INTER_CUBIC : 크기 늘릴 때 사용(속도 느림, 퀄리티 좋음)
# cv2.INTER_LINEAR : 크기 늘릴 때 사용(기본값)

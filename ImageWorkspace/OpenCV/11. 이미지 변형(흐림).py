import cv2

img = cv2.imread("img.jpg")

# 1. 커널 사이즈 변화에 따른 흐림
kernel_3 = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=0)
kernel_5 = cv2.GaussianBlur(img, ksize=(5, 5), sigmaX=0)
kernel_7 = cv2.GaussianBlur(img, ksize=(7, 7), sigmaX=0)

cv2.imshow("image", img)
cv2.imshow("GaussianBlur(Kernel Size 3)", kernel_3)
cv2.imshow("GaussianBlur(Kernel Size 5)", kernel_5)
cv2.imshow("GaussianBlur(Kernel Size 7)", kernel_7)

# 2. 표준 편차 변화에 따른 흐림
sigma_1 = cv2.GaussianBlur(img, ksize=(0, 0), sigmaX=1) # sigmaX : 카우시안 커널의 x 방향의 표준 편차
sigma_2 = cv2.GaussianBlur(img, ksize=(0, 0), sigmaX=2)
sigma_3 = cv2.GaussianBlur(img, ksize=(0, 0), sigmaX=3)

cv2.imshow("GaussianBlur(SigmaX 1)", sigma_1)
cv2.imshow("GaussianBlur(SigmaX 2)", sigma_2)
cv2.imshow("GaussianBlur(SigmaX 3)", sigma_3)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

#########################################################
# 이미지 저장
img = cv2.imread("ImageWorkspace/OpenCV/img.jpg", cv2.IMREAD_GRAYSCALE)
result = cv2.imwrite("img_grayscale.png", img)  # PNG 형태로 저장
print(result)
#########################################################

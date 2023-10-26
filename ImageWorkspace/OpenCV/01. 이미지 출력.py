import cv2

# cv2.IMREAD_COLOR : 컬러 이미지, 투명 영역은 무시함(기본값)
# cv2.IMREAD_GRAYSCALE : 흑백 이미지
# cv2.IMREAD_UNCHANGED : 투명 영역까지 포함
img = cv2.imread("ImageWorkspace/OpenCV/img.jpg", cv2.IMREAD_COLOR)

print(f"이미지 높이:{img.shape[0]}, 이미지 너비:{img.shape[1]}, 이미지 채널:{img.shape[2]}")

cv2.imshow('image', img)  # image라는 이름의 창에 img를 표시
cv2.waitKey(0)
cv2.destroyAllWindows()

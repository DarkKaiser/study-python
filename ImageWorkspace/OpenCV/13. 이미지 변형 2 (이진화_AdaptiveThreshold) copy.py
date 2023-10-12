import cv2

#######################################################
# Adaptive Threshold
# 이미지를 작은 영역으로 나누어서 임계치 적용
#######################################################

def empty(pos):
    # print(pos)
    pass

img = cv2.imread("book.jpg", cv2.IMREAD_GRAYSCALE)

name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar("block_size", name, 25, 100, empty)  # 블럭크기는 홀수만 가능, 1보다는 큰 값
cv2.createTrackbar("c", name, 3, 10, empty)  # 일반적으로 양수의 값을 사용

while True:
    block_size = cv2.getTrackbarPos("block_size", name)
    c = cv2.getTrackbarPos("c", name)
    
    # 1 이하면 3으로 변경
    if block_size <= 1:
        block_size = 3
        
    # 짝수이면 홀수로 변경
    if block_size % 2 == 0:
        block_size += 1
    
    binary = cv2.adaptiveThreshold(img, maxValue=255, adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C, thresholdType=cv2.THRESH_BINARY, blockSize=block_size, C=c)

    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

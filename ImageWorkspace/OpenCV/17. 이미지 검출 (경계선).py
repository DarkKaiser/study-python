import cv2

def empty(pos):
    pass

img = cv2.imread("snowman.png")

name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar("threshold1", name, 0, 255, empty)   # 하위 임계값
cv2.createTrackbar("threshold2", name, 0, 255, empty)   # 상위 임계값

while True:
    threshold1 = cv2.getTrackbarPos("threshold1", name)
    threshold2 = cv2.getTrackbarPos("threshold2", name)

    # Canny Edge Detection
    # threshold1 : 하위 임계값
    # threshold2 : 상위 임계값
    canny = cv2.Canny(img, threshold1=threshold1, threshold2=threshold2)

    cv2.imshow("image", img)
    cv2.imshow(name, canny)
    
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

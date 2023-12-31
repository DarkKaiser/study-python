import cv2

def empty(pos):
    # print(pos)
    pass

img = cv2.imread("ImageWorkspace/OpenCV/book.jpg", cv2.IMREAD_GRAYSCALE)

name = "Trackbar"
cv2.namedWindow(name)
cv2.createTrackbar("threshold", name, 127, 255, empty)  # bar 이름, 창의 이름, 초기값, 최대값, 이벤트 처리

while True:
    thresh = cv2.getTrackbarPos("threshold", name)
    ret, binary = cv2.threshold(img, thresh=thresh, maxval=255, type=cv2.THRESH_BINARY)

    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

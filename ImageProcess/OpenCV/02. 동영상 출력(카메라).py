import cv2

cap = cv2.VideoCapture(0)   # 0번째 카메라 장치(Device ID)

if cap.isOpened() == False:
    exit    # 프로그램 종료
    
while True:
    ret, frame = cap.read()
    if ret == False:
        break
    
    cv2.imshow("camera", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2

cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    # ret : 성공여부, frame : 받아온 이미지
    ret, frame = cap.read()
    if ret == False:
        print("더 이상 가져올 프레임이 없습니다!")
        break
    
    cv2.imshow("video", frame)

    if cv2.waitKey(20) == ord('q'):
        print("사용자 입력에 의해 종료합니다.")
        break

cap.release()
cv2.destroyAllWindows() # 모든 창 닫기

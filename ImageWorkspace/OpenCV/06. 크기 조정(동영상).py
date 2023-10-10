import cv2

cap = cv2.VideoCapture("video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if ret == False:
        break
    
    frame_resized = cv2.resize(frame, (400, 500))
    
    cv2.imshow('video', frame_resized)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

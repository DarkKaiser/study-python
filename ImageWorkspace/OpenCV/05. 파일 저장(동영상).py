import cv2

cap = cv2.VideoCapture("ImageWorkspace/OpenCV/video.mp4")

# 코덱 정의
fourcc = cv2.VideoWriter_fourcc(*"DIVX")

fps = cap.get(cv2.CAP_PROP_FPS)
width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter("output.avi", fourcc, fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    
    if ret == False:
        break
    
    out.write(frame)    # 영상 데이터만 저장(소리는 저장되지 않는다)
    
out.release()
cap.release()

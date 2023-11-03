import cv2
import numpy as np

# 세로 480 x 가로 640, 3채널(RGB)에 해당하는 스케치북 만들기
img = np.zeros((480, 640, 3), dtype=np.uint8)

##########################################
# 전체 공간을 흰 색으로 채우기
# img[:] = (255, 255, 255)
##########################################

##########################################
# 일부 영역 색칠
# 세로기준 100~200 사이, 가로기준 200~300 사이에 흰 색으로 칠한다.
img[100:200, 200:300] = (255, 255, 255)
##########################################

##########################################
# 직선
# cv2.LINE_4 : 상하좌우 4방향으로 연결된 선
# cv2.LINE_8 : 대각선을 포함한 8방향으로 연결된 선(기본값)
# cv2.LINE_AA : 부드러운 선(anti-aliasing)
COLOR = (0, 255, 255)   # BGR : Yellow
THICKNESS = 3           # 선 두께

cv2.line(img, (50, 100), (400, 50), COLOR, THICKNESS, cv2.LINE_8)
cv2.line(img, (50, 200), (400, 150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50, 300), (400, 250), COLOR, THICKNESS, cv2.LINE_AA)
##########################################

##########################################
# 원
COLOR = (255, 255, 0)   # BGR : 옥색
RADIUS = 50             # 반지름
THICKNESS = 10          # 두께
cv2.circle(img, (200, 100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)  # 속이 빈 원
cv2.circle(img, (400, 100), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA) # 속이 채워진 원
##########################################

##########################################
# 사각형
COLOR = (0, 255, 0)     # BGR : 초록색
THICKNESS = 3           # 두께
cv2.rectangle(img, (50, 100), (150, 200), COLOR, THICKNESS, cv2.LINE_AA)    # 속이 빈 사각형
cv2.rectangle(img, (50, 300), (150, 400), COLOR, cv2.FILLED, cv2.LINE_AA)    # 속이 채워진 사각형
##########################################

##########################################
# 다각형
COLOR = (0, 0, 255)     # BGR : 빨간색
THICKNESS = 3           # 두께
pts1 = np.array([[100, 100], [200, 100], [100, 200]])
pts2 = np.array([[200, 100], [300, 100], [300, 200]])
cv2.polylines(img, [pts1, pts2], True, COLOR, THICKNESS, cv2.LINE_AA)   # 속이 빈 다각형

pts3 = np.array([[[100, 300], [200, 300], [100, 400]], [[200, 300], [300, 300], [300, 400]]])
cv2.fillPoly(img, pts3, COLOR, cv2.LINE_AA)                             # 속이 채워진 다각형
##########################################

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

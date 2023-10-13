import cv2

# 윤곽선 : 경계선을 연결한 선

img = cv2.imread("card.png")
target_img = img.copy()     # 사본 이미지

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, otsu = cv2.threshold(gray, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# contours : 윤곽선 정보
# hierarchy : 윤곽선 구조
# mode : 윤곽선을 찾는 모드
#   - cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
#   - cv2.RETR_LIST : 모든 윤곽선 찾음(계층 정보 없음)
#   - cv2.RETR_TREE : 도든 윤곽선 찾음(계층 구조를 트리 구조로 생성)
# method : 윤곽선을 찾을 때 사용하는 근사치 방법
contours, hierarchy = cv2.findContours(otsu, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_NONE)
# contours, hierarchy = cv2.findContours(otsu, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
# contours, hierarchy = cv2.findContours(otsu, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)

COLOR = (0, 200, 0) # 녹색
# contours : 윤곽선 정보
# contourIdx : 인덱스(-1이면 전체)
# color : 색깔
# thickness : 두께
cv2.drawContours(target_img, contours, contourIdx=-1, color=COLOR, thickness=2)

# 경계 사각형
# 윤곽선의 경계면을 둘러싸는 사각형
for cnt in contours:
    if cv2.contourArea(cnt) > 25000:    # 윤곽선의 면적이 25000보다 큰 것만 그리도록 한다.
        x, y, width, height = cv2.boundingRect(cnt)
        cv2.rectangle(target_img, (x, y), (x + width, y + height), (200, 0, 0), 2)

cv2.imshow("image", img)
cv2.imshow("target_img", target_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

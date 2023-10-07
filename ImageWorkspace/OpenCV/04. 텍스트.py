import cv2
import numpy as np

# PIL(Python Image Library)
from PIL import ImageFont, ImageDraw, Image

def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)

# OpenCV에서 사용하는 글꼴 종류
# cv2.FONT_HERSHEY_SIMPLEX : 보통 크기의 산세리프 글꼴
# cv2.FONT_HERSHEY_PLAIN : 작은 크기의 산세리프 글꼴
# cv2.FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 스타일 글꼴
# cv2.FONT_HERSHEY_TRIPLEX : 보통 크기의 세리프 글꼴
# cv2.FONT_ITALIC : 기울임(위의 글꼴과 중복해서 사용 가능)

img = np.zeros((480, 640, 3), dtype=np.uint8)

SCALE = 1
COLOR = (255, 255, 255)
THICKNESS = 1

cv2.putText(img, "Simple Text", (20, 50), cv2.FONT_HERSHEY_COMPLEX, SCALE, COLOR, THICKNESS)

# 한글 출력 우회
# OpenCV에서는 한글이 지원되지 않음
img = myPutText(img, "안녕하세요", (20, 150), 30, COLOR)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

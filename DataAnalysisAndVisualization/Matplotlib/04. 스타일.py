import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 04. 스타일

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

x = [1, 2, 3]
y = [2, 4, 8]

# 그래프 라인 두께 설정
# plt.plot(x, y, linewidth=5)
# plt.show()

# 그래프 마커(marker) 설정
# plt.plot(x, y, marker='o')
# plt.plot(x, y, marker='o', linestyle='None')
# plt.plot(x, y, marker='v')
# plt.plot(x, y, marker='v', markersize='10')
# plt.plot(x, y, marker='X', markersize='10')
# plt.plot(x, y, marker='X', markersize='10', markeredgecolor='red')
# plt.plot(x, y, marker='X', markersize='10', markeredgecolor='red' markerfacecolor='yellow')
# plt.show()

# 선 스타일
# plt.plot(x, y, linestyle=':')
# plt.plot(x, y, linestyle='--')
# plt.plot(x, y, linestyle='-.')
# plt.show()

# 색깔
# plt.plot(x, y, color='pink')
# plt.plot(x, y, color='#ff0000')
# plt.plot(x, y, color='b')
# plt.show()

# 포맷
# plt.plot(x, y, 'ro--') # color, marker style, linestyle
# plt.plot(x, y, 'go')
# plt.show()

# 축약어
# plt.plot(x, y, marker='o' mfc='red', ms=10, mec='blue', ls=':')
# plt.show()

# 투명도
# plt.plot(x, y, marker='o' mfc='red', ms=10, alpha=0.3)
# plt.show()

# 그래프 크기
# plt.figure(figsize=(10, 5), dpi=200)
# plt.plot(x, y)
# plt.show()

# 배경
plt.figure(facecolor='yellow')
plt.plot(x, y)
plt.show()

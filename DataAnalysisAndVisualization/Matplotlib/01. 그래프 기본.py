import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 01. 그래프 기본

x = [1, 2, 3]
y = [2, 4, 8]
# plt.plot(x, y)
# plt.show()

# 제목 설정
# plt.title('Line Graph')
# plt.show()

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결
plt.title('꺽은선 그래프')
plt.show()

# 사용 가능한 폰트 목록 확인
import matplotlib.font_manager as fm
# fm.fontManager.ttflist
# [print(f.name) for f in fm.fontManager.ttflist]

# 가로/세로 좌표출에 마이너스('-')가 포함된 그래프 출력
# plt.plot([-1, 0, 1], [-5, -1, 2])
# plt.show()

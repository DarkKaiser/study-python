import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 03. 범례(legend)

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

x = [1, 2, 3]
y = [2, 4, 8]

# plt.plot(x, y, label='무슨 데이터')
# plt.legend()
# plt.show()

# plt.plot(x, y, label='무슨 데이터')
# plt.legend(loc='upper right')
# plt.show()

# plt.plot(x, y, label='무슨 데이터')
# plt.legend(loc='best')
# plt.show()

plt.plot(x, y, label='범례')
plt.legend(loc=(0.5, 0.5)) # X축, Y축(0 ~ 1 사이)
plt.show()

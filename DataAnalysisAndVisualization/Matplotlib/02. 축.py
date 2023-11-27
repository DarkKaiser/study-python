import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 02. 축

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

x = [1, 2, 3]
y = [2, 4, 8]

plt.plot(x, y)
plt.title('꺽은선 그래프', fontdict={'family':'Malgun Gothic', 'size':20})
plt.xlabel('X축', color='red')
plt.ylabel('Y축', color='#00aa00')
# plt.show()

plt.xlabel('X축', color='red', loc='right') # left, center, right
plt.ylabel('Y축', color='#00aa00', loc='top') # top, center, bottom
# plt.show()

plt.xticks([1, 2, 3])
plt.yticks([3, 6, 9, 12])
plt.show()

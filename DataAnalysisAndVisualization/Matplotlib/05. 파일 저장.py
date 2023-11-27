import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 05. 파일 저장

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

x = [1, 2, 3]
y = [2, 4, 8]

# plt.plot(x, y)
# plt.savefig('graph.png')
# plt.savefig('graph.png', dpi=100)

plt.figure(dpi=200)
plt.plot(x, y)
plt.savefig('graph_200.png', dpi=100)

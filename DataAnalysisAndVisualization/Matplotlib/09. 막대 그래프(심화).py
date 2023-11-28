import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 09. 막대 그래프(심화)

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

labels = ['강백호', '서태웅', '정대만'] # 이름
values = [190, 187, 184] # 키

# plt.barh(labels, values)
# plt.show()

# bar = plt.bar(labels, values)
# bar[0].set_hatch('/') # /////
# bar[1].set_hatch('x') # xxxxx
# bar[2].set_hatch('..') # ....
# plt.show()

bar = plt.bar(labels, values)
for idx, rect in enumerate(bar):
    plt.text(idx, rect.get_height() + 0.5, values[idx], ha='center', color='blue')
plt.show()

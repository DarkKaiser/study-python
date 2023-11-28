import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 08. 막대 그래프

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

labels = ['강백호', '서태웅', '정대만'] # 이름
values = [190, 187, 184] # 키
colors = ['r', 'g', 'b']
ticks = ['1번학생', '2번학생', '3번학생']

# plt.bar(labels, values)
# plt.bar(labels, values, color='r')
# plt.bar(labels, values, color=colors)
# plt.bar(labels, values, color=colors, alpha=0.5)
# plt.bar(labels, values, width=0.5)
# plt.show()

# plt.bar(labels, values)
# plt.ylim(175, 195) # Y축의 데이터 범위 지정
# plt.show()

# plt.bar(labels, values, width=0.3)
# plt.xticks(rotation=45) # X축의 이름 데이터 각도를 45도로 설정
# plt.yticks(rotation=45) # Y축의 키 데이터 각도를 45도로 설정
# plt.show()

plt.bar(labels, values)
plt.xticks(labels, ticks) # X축의 레이블을 이름이 아닌 번호가 나오도록 수정
plt.show()

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 15. 산점도 그래프

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

df = pd.read_excel('score.xlsx')

df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2]

# --------------------------------------------

# plt.scatter(df['영어'], df['수학'])
# plt.xlabel('영어 점수')
# plt.ylabel('수학 점수')
# plt.show()

# --------------------------------------------

# sizes = np.random.rand(8) * 1000

# plt.scatter(df['영어'], df['수학'], s=sizes)
# plt.xlabel('영어 점수')
# plt.ylabel('수학 점수')
# plt.show()

# --------------------------------------------

sizes = df['학년'] * 500

plt.figure(figsize=(7, 7))
plt.scatter(df['영어'], df['수학'], s=sizes, c=df['학년'], cmap='viridis', alpha=0.3)
plt.xlabel('영어 점수')
plt.ylabel('수학 점수')
plt.colorbar(ticks=[1, 2, 3], label='학년', shrink=0.3)
plt.show()

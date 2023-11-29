import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 16. 여러 그래프

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

df = pd.read_excel('score.xlsx')

# --------------------------------------------

fig, axs = plt.subplots(2, 2, figsize=(15, 10)) # 2 X 2 에 해당하는 plot들을 생성
fig.suptitle('여러 그래프 넣기')

# 첫 번째 그래프
axs[0, 0].bar(df['이름'], df['국어'], label='국어 점수') # 데이터 설정
axs[0, 0].set_title('첫 번째 그래프') # 제목
axs[0, 0].legend() # 범례
axs[0, 0].set(xlabel='이름', ylabel='점수') # x, y축 Label
axs[0, 0].set_facecolor('lightyellow') # 전면색
axs[0, 0].grid(linestyle='--', linewidth=0.5)

# 두 번째 그래프
axs[0, 1].plot(df['이름'], df['수학'], label='수학')
axs[0, 1].plot(df['이름'], df['영어'], label='영어')
axs[0, 1].legend()

# 세 번째 그래프
axs[1, 0].barh(df['이름'], df['키'])

# 네 번째 그래프
axs[1, 1].plot(df['이름'], df['사회'], color='green', alpha=0.5)

plt.show()

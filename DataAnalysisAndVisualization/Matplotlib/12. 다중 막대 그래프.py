import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 11. 누적 막대 그래프

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

df = pd.read_excel('score.xlsx')

N = df.shape[0]
index = np.arange(N)

w = 0.25
plt.bar(index - w, df['국어'], width=w, label='국어')
plt.bar(index, df['영어'], width=w, label='영어')
plt.bar(index + w, df['수학'], width=w, label='수학')
plt.legend(ncol=3)
plt.xticks(index, df['이름'], rotation=60)
plt.show()

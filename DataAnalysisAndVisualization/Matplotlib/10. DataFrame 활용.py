import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 10. DataFrame 활용

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

df = pd.read_excel('score.xlsx')

# plt.plot(df['지원번호'], df['키'])
# plt.show()

# 2개의 데이터를 넣어서 출력
plt.plot(df['지원번호'], df['영어'])
plt.plot(df['지원번호'], df['수학'])
plt.grid()
# plt.grid(axis='x', color='purple', alpha=0.2, linestyle='--')
plt.show()

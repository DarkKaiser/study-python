import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 11. 누적 막대 그래프

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

df = pd.read_excel('score.xlsx')

# 누적 막대 그래프를 사용하지 않으면 값이 겹쳐져서 출력된다.
# plt.bar(df['이름'], df['국어'])
# plt.bar(df['이름'], df['영어'])
# plt.show()

# 누적 막대 그래프로 출력
plt.bar(df['이름'], df['국어'])
plt.bar(df['이름'], df['영어'], bottom=df['국어'])
plt.bar(df['이름'], df['수학'], bottom=df['영어'] + df['영어'])
plt.show()

import matplotlib
import matplotlib.pyplot as plt

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 07. 여러 데이터

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

x = [1, 2, 3]
y = [2, 4, 8]

# COVID-19 백신 종류별 접종 인구
days = [1, 2, 3] # 1일, 2일, 3일
az = [2, 4, 8] # (단위 : 만명) 1일부터 3일까지 아스트라제니카 접종 인구
pfizer = [5, 1, 3] # 화이자
moderna = [1, 2, 5] # 모더나

plt.plot(days, az, label='az')
plt.plot(days, pfizer, label='pfizer', marker='o', linestyle='--')
plt.plot(days, moderna, label='moderna', marker='s', linestyle='-.')
plt.legend()
plt.show()

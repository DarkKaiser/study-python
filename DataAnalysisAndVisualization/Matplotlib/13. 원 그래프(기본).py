import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 13. 원 그래프(기본)

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
explode = [0.2, 0.1, 0, 0, 0, 0]

# plt.pie(values, labels=labels, autopct='%.1f%%')
# plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90)
# plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False)
# plt.pie(values, labels=labels, explode=explode)
# plt.show()

plt.pie(values, labels=labels, explode=explode)
plt.legend(loc=(1.2, 0.3), title='언어별 선호도')
plt.show()

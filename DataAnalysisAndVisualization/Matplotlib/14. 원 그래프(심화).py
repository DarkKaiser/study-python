import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Matplotlib
# 다양한 형태의 그래프를 통하여 데이터 시각화를 할 수 있는 라이브러리
# 14. 원 그래프(심화)

# 한글 제목 폰트 설정
matplotlib.rcParams['font.size'] = 15 # 글자 크기
matplotlib.rcParams['font.family'] = 'HYGungSo-Bold' # 궁서체
matplotlib.rcParams['axes.unicode_minus'] = False # 한글 폰트 사용시, 마이너스('-') 글자가 깨지는 현상을 해결

values = [30, 25, 20, 13, 10, 2]
labels = ['Python', 'Java', 'Javascript', 'C#', 'C/C++', 'ETC']
colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff', '#a0c4ff']
explode = [0.05] * 6

# plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, explode=explode)
# plt.show()

# wedgeprops = {'width':0.6}
# plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, explode=explode, wedgeprops=wedgeprops)
# plt.show()

# wedgeprops = {'width':0.6, 'edgecolor':'w', 'linewidth':2}
# plt.pie(values, labels=labels, autopct='%.1f%%', startangle=90, counterclock=False, colors=colors, explode=explode, wedgeprops=wedgeprops)
# plt.show()

# --------------------------------------------

# 10% 이상만 출력
# def custom_autopct(pct):
#     return ('%.1f%%' % pct) if pct >= 10 else ''

# wedgeprops = {'width':0.6, 'edgecolor':'w', 'linewidth':2}
# plt.pie(values, labels=labels, autopct=custom_autopct, startangle=90, counterclock=False, colors=colors, explode=explode, wedgeprops=wedgeprops, pctdistance=0.7)
# plt.show()

# --------------------------------------------

# DataFrame 활용
df = pd.read_excel('score.xlsx')
grp = df.groupby('학교')
values = [grp.size()['북산고'], grp.size()['능남고']]
labels = ['북산고', '능남고']

plt.pie(values labels=labels)
plt.title('소속 학교')
plt.show()

# --------------------------------------------

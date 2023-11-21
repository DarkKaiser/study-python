import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 1. Series
#    1차원 데이터(정수, 실수, 문자열 등)

# Series 객체 생성
# 예) 1월부터 4월까지의 평균 온도 데이터(-20, -10, 10, 20)
temp = pd.Series([-20, -10, 10, 20])
print(temp)
print(temp[0]) # 1월 온도

# Series 객체 생성(Index 지정)
# 예) 1월부터 4월까지의 평균 온도 데이터(-20, -10, 10, 20)
temp = pd.Series([-20, -10, 10, 20], index=['Jan', 'Feb', 'Mar', 'Apr'])
print(temp)
print(temp['Jan'])

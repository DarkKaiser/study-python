import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 8. 데이터 선택(iloc)
#    위치를 이용하여 원하는 row에서 원하는 col 선택

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

print(df.iloc[0]) # 0번째 Index에 해당하는 데이터

print(df.iloc[0:5]) # 0 ~ 4번째 Index에 해당하는 데이터

print(df.iloc[0, 1]) # 0번째 위치의 1번째(학교) 데이터

print(df.iloc[[0, 1], 2]) # 0, 1번째 위치의 학생의 2번째(키) 데이터

print(df.iloc[0:5, 3:8]) # 0 ~ 4번째 위치의 학생 중에서 3 ~ 7번째(국어:사회) 데이터

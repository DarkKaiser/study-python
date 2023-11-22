import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 10. 결측치
#     비어있는 데이터

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

# 데이터 채우기 fillna
print(df.fillna('')) # 전체 NaN 데이터를 빈칸으로 채움
print(df['SW특기'].fillna('확인 중')) # SW특기 데이터 중에서 NaN 데이터를 채움

# 데이터 제외하기 dropna
print(df.dropna()) # 전체 데이터 중에서 NaN을 포함하는 데이터 삭제
print(df.dropna(axis='index', how='any')) # axis(index or columns), how(any or all), NaN 데이터가 하나라도 있는 row를 삭제
print(df.dropna(axis='columns', how='any')) # axis(index or columns), how(any or all), NaN 데이터가 하나라도 있는 column을 삭제
print(df.dropna(axis='columns', how='all')) # axis(index or columns), how(any or all), column 데이터 전체가 NaN인 경우에만 column을 삭제

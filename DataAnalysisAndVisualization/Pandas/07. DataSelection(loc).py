import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 7. 데이터 선택(loc)
#    이름을 이용하여 원하는 row에서 원하는 col 선택

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

print(df.loc['5번']) # Index '5번'에 해당하는 전체 row 데이터

print(df.loc['5번', '국어']) # Index '5번'에 해당하는 국어 데이터

print(df.loc[['1번', '2번'], '국어']) # Index '1번', '2번'에 해당하는 국어 데이터

print(df.loc['1번':'5번', '국어']) # Index '1번'부터 '5번'까지 국어 데이터

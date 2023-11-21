import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 5. 데이터 확인

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

#
# DataFrame 확인
#

# 계산 가능한 데이터에 대해 Column 별로 데이터의 갯수, 평균, 표준편차, 최소/최대값등의 정보를 보여줌
print(df.describe())

print(df.info())

# 처음 5개의 row를 가져옴
print(df.head())

# 처음 7개의 row를 가져옴
print(df.head(7))

# 마지막 5개의 row를 가져옴
print(df.tail())

print(df.values())

print(df.index())

print(df.columns())

# row, column 갯수
print(df.shape())

#
# Series 확인
#
print(df['키'].describe())

print(df['키'].nlargest(3)) # 키 큰 사람 순서대로 3명의 데이터를 출력

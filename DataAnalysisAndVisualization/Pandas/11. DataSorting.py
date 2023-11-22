import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 11. 데이터 정렬

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

print(df.sort_values('키')) # 키 기준으로 오름차순 정렬
print(df.sort_values('키', ascending=False)) # 키 기준으로 내림차순 정렬
print(df.sort_values(['수학', '영어'], ascending=False)) # 수학, 영어 기준으로 내림차순 정렬
print(df.sort_values(['수학', '영어'], ascending=[True, False])) # 수학 점수는 오름차순, 영어 점수는 내림차순으로 정렬

print(df['키'].sort_values())

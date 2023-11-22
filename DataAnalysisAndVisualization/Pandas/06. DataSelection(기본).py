import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 6. 데이터 선택(기본)

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

# 컬럼 선택(Label)
print(df['이름'])
print(df['키'])
print(df[['이름', '키']])

# 컬럼 선택(정수 Index)
print(df[df.columns[0]])
print(df[df.columns[-1]]) # 맨 끝에 있는 값을 가져옴

# 슬라이싱
print(df['영어'][0:5]) # 0 ~ 4 까지의 영어 점수 데이터 가져옴
print(df[3:]) # 전체 데이터 중에서 4번째 줄부터 끝 줄까지의 데이터 가져옴

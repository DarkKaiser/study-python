import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 14. 그룹화
#     동일한 값을 가진 것들끼리 합쳐서 통계 또는 평균 등의 값을 계산하기 위해 사용

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

print(df.groupby('학교').get_group('북산고'))

# print(df.groupby('학교').mean()) # 계산 가능한 데이터들의 평균값
print(df.groupby('학교')['키'].mean()) # 학교로 그룹화를 한 뒤에 키의 평균 데이터
print(df.groupby('학교')[['국어', '영어', '수학']].mean()) # 학교로 그룹화를 한 뒤에 국어, 영어, 수학의 평균 데이터

print(df.groupby('학교').size()) # 각 그룹의 크기
print(df.groupby('학교').size()['능남고']) # 학교로 그룹화를 한 뒤에 능남고에 해당하는 데이터의 수

df['학년'] = [3, 3, 2, 1, 1, 3, 2, 2] # 학년 컬럼 추가

print(df.groupby(['학교', '학년'])[['국어', '영어', '수학']].mean()) # 학교별, 학년별 국어, 영어, 수학 평균 데이터

print(df.groupby('학년')[['키', '국어', '영어', '수학']].mean().sort_values('키')) # 학년별 국어, 영어, 수학 평균 데이터를 키를 기준으로 정렬

print(df.groupby('학교')[['이름', 'SW특기']].count()) # 학교로 그룹화를 한 뒤에 각 학교별 SW특기 데이터의 수를 가져옴

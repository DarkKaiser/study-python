import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 12. 데이터 수정

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

# 컬럼 수정
print(df['학교'].replace({'북산고':'상북고', '능남고':'무슨고'})) # 북산고->상북고, 능남고->무슨고로 변경

df['SW특기'] = df['SW특기'].str.lower() # SW특기 데이터를 모두 소문자로 변경
print(df)

df['학교'] = df['학교'] + '등학교' # 학교이름+등학교
print(df)

# 컬럼 추가
df['총합'] = df['국어'] + df['영어'] + df['수학'] + df['과학'] + df['사회']
print(df)

df['결과'] = 'Fail' # 결과 컬럼을 추가하고 전체 데이터는 Fail로 초기화

df.loc[df['총합'] > 400, '결과'] = 'Pass' # 총합이 400보다 큰 데이터에 대해서 결과를 Pass로 업데이트
print(df)

# 컬럼 삭제
df.drop(columns=['총합']) # 총합 컬럼 삭제

# Row 삭제
df.drop(index='4번') # 4번 학생 데이터 Row 삭제

filt = df['수학'] < 80 # 수학 점수가 80점 미만인 학생 필터링
df.drop(index=df[filt].index) # 수학 점수가 80점 미만인 학생 Row 삭제

# Row 추가
df.loc['9번'] = ['이정환', '해남고등학교', 184, 90, 90, 90, 90, 90, 'Kotlin', 450, 'Pass']
print(df)

# Cell 수정
df.loc['4번', 'SW특기'] = 'Python' # 4번 학생의 SW특기 데이터를 Python으로 수정
df.loc['5번', ['학교', 'SW특기']] = ['능남고등학교', 'C'] # 5번 학생의 학교는 능남고등학교로, SW특기는 C로 수정

# 컬럼 순서 변경
cols = list(df.columns)
df = df[[cols[-1]] + cols[0:-1]] # 맨 뒤에 있는 결과 컬럼을 앞으로 가져오고, 나머지 컬럼들과 합쳐서 순서 변경
print(df)

# 컬럼 이름 변경
df.columns = ['Result', 'Name', 'School', '키', '국어', '영어', '수학', '과학', '사회', 'SW특기', '총합']
print(df)

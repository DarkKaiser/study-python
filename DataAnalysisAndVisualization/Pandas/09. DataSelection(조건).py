import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 9. 데이터 선택(조건)
#    조건에 해당하는 데이터 선택

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

print(df['키'] >= 185) # 학생들의 키가 185 이상인지의 여부를 True/False로 출력

filt = (df['키'] >= 185)
print(df[filt]) # 키가 185 이상인 학생들만 가져옴 
print(df[~filt]) # 키가 185 미만인 학생들만 가져옴 

print(df.loc[df['키'] >= 185, '수학']) # 키가 185 이상인 학생들의 수학 데이터

# AND 조건
print(df.loc[(df['키'] >= 185) & (df['학교'] == '북산고')]) # 키가 185 이상인 북산고 학생들의 데이터

# OR 조건
print(df.loc[(df['키'] < 170) | (df['키'] > 200)]) # 키가 170보다 작거나 200보다 큰 학생들의 데이터

# str 함수
filt = df['이름'].str.startswith('송') # '송'씨 성을 가진 사람
print(df[filt])
filt = df['이름'].str.contains('태') # 이름에 '태'가 들어간 사람
print(df[filt])
print(df[~filt]) # 이름에 '태'가 들어간 사람을 제외

# isin(대소문자 구분)
langs = ['Python', 'Java']
filt = df['SW특기'].isin(langs) # SW특기가 Python이거나 Java인 사람
print(df[filt])

# isin(대소문자 구분하지 않음)
langs = ['python', 'java']
filt = df['SW특기'].str.lower().isin(langs) # SW특기가 Python이거나 Java인 사람
print(df[filt])

# SW특기 값 중에서 Java라는 글자를 포함하는 사람
filt = df['SW특기'].str.contains('Java', na=False) # NaN 데이터에 대해서 False로 설정
print(df[filt])

import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 4. 파일 저장 및 열기
#    DataFrame 객체를 Excel, CSV, TXT등 형태의 파일로 저장 및 열기

# Data 준비
data = {
    '이름' : ['채치수', '정대만', '송태섭', '서태웅', '강백호', '변덕규', '황태산', '윤대협'],
    '학교' : ['북산고', '북산고', '북산고', '북산고', '북산고', '능남고', '능남고', '능남고'],
    '키' : [197, 184, 168, 187, 188, 202, 188, 190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

df = pd.DataFrame(data, index=['1번', '2번', '3번', '4번', '5번', '6번', '7번', '8번'])
df.index.name = '지원번호'
print(df)

# CSV 파일로 저장
df.to_csv('score.csv', encoding='utf-8-sig')
# df.to_csv('score.csv', encoding='utf-8-sig', index=False) # Index는 제외하고 저장

# TXT 파일로 저장
df.to_csv('score.txt', sep='\t') # TAB으로 구분된 텍스트 파일

# Excel 파일로 저장
df.to_excel('score.xlsx')

####################################################################################

# CSV 파일 열기
df = pd.read_csv('score.csv')
print(df)
df = pd.read_csv('score.csv', skiprows=1) # 지정된 갯수 만큼의 row를 건너뜀
print(df)
df = pd.read_csv('score.csv', skiprows=[1, 3, 5]) # 1, 3, 5 row는 제외(row는 0부터 시작)
print(df)
df = pd.read_csv('score.csv', nrows=4) # 지정된 갯수 만큼의 row만 가져옴
print(df)
df = pd.read_csv('score.csv', skiprows=2, nrows=4) # 처음 2개의 row는 무시하고 이후에 4개의 row만 가져옴
print(df)

# TXT 파일 열기
df = pd.read_csv('score.txt', sep='\t', index_col='지원번호')
print(df)

# Excel 파일 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

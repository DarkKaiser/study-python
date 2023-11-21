import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 3. Index
#    데이터에 접근할 수 있는 주소값

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
print(df)
print(df.index)

# Index 이름 설정
df.index.name = '지원번호'
print(df)

# Index 초기화
print(df.reset_index()) # Index를 초기화(새로운 인덱스 추가)하면서, 기존 지원번호 인덱스는 컬럼 형식으로 변환, 실제 데이터에는 반영 안됨
print(df.reset_index(drop=True)) # Index를 초기화(새로운 인덱스 추가)하면서 기존 지원번호 인덱스는 삭제됨, 실제 데이터에는 반영 안됨 
print(df)
df.reset_index(drop=True, inplace=True) # 실제 데이터에 바로 반영
print(df)

# 지정한 컬럼을 Index로 설정
df.set_index('이름', inplace=True)
print(df)

# Index를 기준으로 오름차순, 내림차순 정렬
df.sort_index(inplace=True) # 인덱스로 오름차순 정렬
print(df)

df.sort_index(ascending=False, inplace=True) # 인덱스로 내림차순 정렬
print(df)

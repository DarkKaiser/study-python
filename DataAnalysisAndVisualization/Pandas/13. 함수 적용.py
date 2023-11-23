import pandas as pd

# Pandas
# 파이썬에서 사용하는 데이터 분석 라이브러리
# 13. 함수 적용

# Excel 파일을 열어서 데이터 열기
df = pd.read_excel('score.xlsx', index_col='지원번호')
print(df)

# 키 뒤에 cm을 붙이는 함수
def add_cm(height):
    return str(height) + 'cm'

# 첫 문자는 대문자로, 나머지는 소문자로 변경하는 함수
def capitalize(lang):
    if pd.notnull(lang): # NaN이 아닌지 확인
        return lang.capitalize() # 첫 글자는 대문자로, 나머지는 소문자로
    return lang

# 데이터에 함수 적용(apply)
df['키'] = df['키'].apply(add_cm) # 키 데이터에 대해서 add_cm 함수를 호출한 결과 데이터를 반영
print(df)

df['SW특기'] = df['SW특기'].apply(capitalize) # SW특기 데이터에 대해서 첫 글자는 대문자로, 나머지는 소문자로 변경
print(df)

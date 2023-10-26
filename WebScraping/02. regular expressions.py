import re

def print_match(m):
    print("====================================")
    if m:
        print("m.group():", m.group())  # 일치하는 문자열을 반환
        print("m.string:", m.string)    # 입력받은 문자열
        print("m.start():", m.start())  # 일치하는 문자열의 시작 인덱스
        print("m.end():", m.end())      # 일치하는 문자열의 끝 인덱스
        print("m.span():", m.span())    # 일치하는 문자열의 시작 / 끝 인덱스
    else:
        print("매칭되지 않았습니다.")

# '.' : 하나의 문자를 의미
# '^' : 문자열의 시작
# '$' : 문자열의 끝
p = re.compile("ca.e")

# match : 주어진 문자열의 처음부터 일치하는지 확인
m = p.match("case")
print_match(m)

m = p.match("good care")
print_match(m)

m = p.match("careless")
print_match(m)

m = p.match("xxcare")
print_match(m)

# search : 주어진 문자열중에 일치하는게 있는지 확인
m = p.search("good care")
print_match(m)

m = p.search("careless")
print_match(m)

print("====================================")

# findall : 일치하는 모든것을 리스트 형태로 반환
lst = p.findall("careless")
print(lst)

lst = p.findall("careless good care caxeks")
print(lst)

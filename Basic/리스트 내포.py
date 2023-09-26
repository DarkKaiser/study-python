# 리스트 내포
# 반복 가능한 것을 기반으로 새로운 리스트를 만들어내는 문법
A = [2 * i + 1 for i in range(0, 10)]
print(A)

A = [
    2 * i + 1               # 표현식
    for i in range(0, 10)   # 반복절
    if i % 2 == 0           # 조건절
]
print(A)

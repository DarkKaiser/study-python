# map
def power(숫자):
    return 숫자 ** 2

# power 콜백 함수를 넘긴다.
A = [1, 2, 3, 4, 5]
iter = map(power, A)
print(list(iter))
#for i in iter:
#    print(i)

# filter
def 홀수인가요(숫자):
    if 숫자 % 2 == 1:
        return True
    return False

A = [1, 2, 3, 4, 5]
이터레이터 = filter(홀수인가요, A)
print(list(이터레이터))

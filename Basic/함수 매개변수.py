# 가변 매개변수
def print_n_times(횟수, *리스트):
    for i in range(횟수):
        for 요소 in 리스트:
            print(요소)
            
print_n_times(2, "안녕", "하세요")

############################################

# 가변 매개변수 + 키워드 매개변수
def print_n_times2(*리스트, 횟수):
    for i in range(횟수):
        for 요소 in 리스트:
            print(요소)

print_n_times2("안녕", "하세요", 횟수=2)

############################################

# 기본 매개변수
def test(a = 10, b = 20):
    print(a, b)
    
test()
test(b = 30)

############################################

# 딕셔너리 매개변수
def dict(**딕셔너리):
    print(딕셔너리)
    
dict(a=10, b=20, c=30, d=40)

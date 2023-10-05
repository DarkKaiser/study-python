# 클래스
class 학생:
    def __init__(self, 이름, 국어):
        self.이름 = 이름
        self.국어 = 국어
        self.__hidden = 0

# 객체 생성
인성 = 학생("인성", 80)

# 변수 추가
인성.이름2 = "인성"

# 변수 사용
print(인성.이름)
print(인성.이름2)
print(인성.__hidden)

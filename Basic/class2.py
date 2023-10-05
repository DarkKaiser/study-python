# 여담: 사실 비교 연산자로 "학생의 성적을 비교할 것이다"는 의도를 알아채기 힘듭니다.
# 그래서 이런 식으로 구현하시면 안 됩니다[그냥 예입니다]. 아래 값 객체 예처럼 사용해주세요.
class Student:
    def __init__(self, 이름, 국어, 영어, 수학, 과학):
        self.이름 = 이름
        self.국어 = 국어
        self.영어 = 영어
        self.수학 = 수학
        self.과학 = 과학
    def sum(self):
        return self.국어 + self.수학 + self.영어 + self.과학
    def average(self):
        return self.sum() / 4
    def print(self):
        print(self.이름, self.sum(), self.average(), sep="\t")
    def __str__(self):
        return f"{self.이름}\t{self.sum()}\t{self.average()}"
    def __eq__(self, 다른대상): # self == 다른대상
        if type(다른대상) == Student:
            return self.sum() == 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() == 다른대상
        else:
            raise "같은 자료형을 비교해주세요"
    def __ne__(self, 다른대상): # self != 다른대상
        if type(다른대상) == Student:
            return self.sum() != 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() != 다른대상
        else:
            raise "같은 자료형을 비교해주세요"
    def __gt__(self, 다른대상): # self > 다른대상
        if type(다른대상) == Student:
            return self.sum() > 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() > 다른대상
        else:
            raise "같은 자료형을 비교해주세요"
    def __ge__(self, 다른대상): # self >= 다른대상
        if type(다른대상) == Student:
            return self.sum() >= 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() >= 다른대상
        else:
            raise "같은 자료형을 비교해주세요"
    def __lt__(self, 다른대상): # self < 다른대상
        if type(다른대상) == Student:
            return self.sum() < 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() < 다른대상
        else:
            raise "같은 자료형을 비교해주세요"
    def __le__(self, 다른대상): # self <= 다른대상
        if type(다른대상) == Student:
            return self.sum() <= 다른대상.sum()
        elif type(다른대상) == int:
            return self.sum() <= 다른대상
        else:
            raise "같은 자료형을 비교해주세요"

class StudentList:
    def __init__(self):
        self.__students = []
    def add(self, student):
        self.__students.append(student)
    def print(self):
        print("이름", "총점", "평균", sep="\t")
        for student in self.__students:
            student.print()
    def __str__(self):
        output = "이름\t총점\t평균\n"
        for student in self.__students:
            output += f"{str(student)}\n"
        return output.strip()
    def clone(self):
        output = StudentList()
        for student in self.__students:
            output.add(student)
        return output
    def __add__(self, 다른대상):
        output = self.clone()
        output.add(다른대상)
        return output

students = StudentList()
students += Student("인성", 87, 88, 98, 95)
students += Student("구름", 92, 98, 97, 98)
students.add(Student("별이", 76, 96, 95, 90))
print(students)

# 값 객체 예
class CmLength:
    # 유효한 값만 객체로 만들게 조건문을 걸었습니다.
    def __init__(self, cm):
        if cm < 0:
            raise "길이는 0 이상으로 지정해야 합니다."
        self.__length = cm
    # 이게 뭔지는 다다음 강의에서 자세하게 다루겠습니다.
    def get():
        return self.__length
    # __sub__, __mul__, __truediv__, __floordiv__ 등도 비슷하게 구현하면 됩니다.
    def __add__(self, 다른대상):
        if type(다른대상) != CmLength:
            raise "길이 단위를 통일해주세요!"
        return CmLength(self.get() + 다른대상.get())
    # 다른 비교 연산자도 다음과 비슷하게 구현하면 됩니다.
    def __eq__(self, 다른대상):
        if type(다른대상) != CmLength:
            raise "같은 자료형끼리만 비교할 수 있습니다."
        return self.get() == 다른대상.get()
    def __ne__(self, 다른대상):
        return not (self == 다른대상)

CmLength(3) + CmLength(10)
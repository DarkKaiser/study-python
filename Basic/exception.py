입력 = input("정수 입력> ")

try:
    숫자입력 = int(입력)
    print(f"원의 반지름 : {숫자입력}")
    print(f"원의 둘레 : {2 * 3.14 * 숫자입력}")
except ValueError as e:
    print("정수를 입력하지 않았습니다.")
except:
    print("예외가 발생하였습니다.")
    raise Exception("예외를 강제로 발생")
else:
    # 예외가 발생하지 않았을 때 실행할 코드
    print("예외가 발생하지 않음")
finally:
    print("finally")
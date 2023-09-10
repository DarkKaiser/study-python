import random

MIN_NUMBER = 1
MAX_NUMBER = 100


def main():
    retry_count = 0
    max_retry_count = 6
    guess_number = random.randint(MIN_NUMBER, MAX_NUMBER)

    print(f"숫자 맞추기 게임입니다.")
    print(f"입력 가능한 총 횟수는 {max_retry_count}회입니다.", end="\n\n")

    input_number = ""
    while retry_count < max_retry_count:
        print(f"{MIN_NUMBER} ~ {MAX_NUMBER} 사이의 숫자를 입력하세요: ", end="")

        input_number = int(input())
        if input_number < guess_number:
            print(f"틀렸습니다. {input_number}보다 큽니다.")
        elif input_number > guess_number:
            print(f"틀렸습니다. {input_number}보다 작습니다.")
        else:
            break

        retry_count += 1

    print("")

    if input_number == guess_number:
        print(f"정답입니다.")
    else:
        print(f"실패하였습니다. 정답은 {guess_number} 입니다.")


if __name__ == '__main__':
    main()

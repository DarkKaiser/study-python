import random


def get_guess_numbers(num_guesses):
    while True:
        print(f'추측 #{num_guesses} : ', end='')

        numbers = input()
        if len(numbers) != 3:
            print('중복되지 않는 숫자 3개만 입력 가능합니다. 다시 입력하세요!')
        elif numbers.isdigit() is False:
            print('숫자만 입력 가능합니다. 다시 입력하세요!')
        elif len(''.join(set(numbers))) != 3:
            print('중복된 숫자가 포함되어 있습니다. 다시 입력하세요!')
        else:
            return list(map(int, numbers))


def get_secret_numbers(num_digits):
    numbers = list(range(10))
    random.shuffle(numbers)
    return numbers[:num_digits]


def get_clues(guess_numbers, secret_numbers):
    if guess_numbers == secret_numbers:
        return '정답입니다.'

    ball = 0
    strike = 0
    for i in range(len(guess_numbers)):
        if guess_numbers[i] == secret_numbers[i]:
            strike += 1
        elif guess_numbers[i] in secret_numbers:
            ball += 1

    if strike == 0 and ball == 0:
        return f'  > 결과 : {len(secret_numbers)}아웃'

    return f'  > 결과 : {strike}스트라이크 {ball}볼'


def play_again():
    print('게임을 다시 시작하시겠습니까? (yes or no)')
    return input().lower().startswith('y')


# 맞힐 숫자 자릿수
NUM_DIGITS = 3

# 최대 추측 횟수
MAX_GUESS = 10


def main():
    print('숫자야구게임에 오신것을 환영합니다.')
    print()

    while True:
        secret_numbers = get_secret_numbers(NUM_DIGITS)
        print(f'0~9 사이의 숫자 {NUM_DIGITS}개를 정했습니다. 총 {MAX_GUESS}번의 추측으로 맞춰보세요!')
        print(secret_numbers)

        num_guesses = 1
        while num_guesses <= MAX_GUESS:
            guess_numbers = get_guess_numbers(num_guesses)
            print(get_clues(guess_numbers, secret_numbers))
            num_guesses += 1

            if guess_numbers == secret_numbers:
                break
            if num_guesses > MAX_GUESS:
                print(f'실패하였습니다. 정답은 {secret_numbers} 이었습니다.')
                break

        if play_again() is False:
            break


if __name__ == '__main__':
    main()

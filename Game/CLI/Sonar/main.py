import math
import random
import sys


def init_board():
    board = []
    for x in range(60):
        board.append([])
        for y in range(15):
            if random.randint(0, 1) == 0:
                board[x].append('~')
            else:
                board[x].append('`')

    return board


def draw_board(board):
    tens_digits_line = '    '
    for i in range(1, 6):
        tens_digits_line += f'{" " * 9}{i}'

    print(tens_digits_line)
    print(f'   {"0123456789" * 6}')

    for row in range(15):
        board_row = ''
        for col in range(60):
            board_row += board[col][row]

        print(f'{row:2} {board_row} {row}')

    print(f'   {"0123456789" * 6}')
    print(tens_digits_line)


def get_treasure_boxs(num_boxs):
    treasure_boxs = []
    while len(treasure_boxs) < num_boxs:
        new_treasure_box = [random.randint(0, 59), random.randint(0, 14)]
        if new_treasure_box in treasure_boxs:
            continue

        treasure_boxs.append(new_treasure_box)

    return treasure_boxs


def is_on_board(x, y):
    return 0 <= x <= 59 and 0 <= y <= 14


def make_moves(board, treasure_boxs, x, y):
    smallest_distance = 100

    # 가장 가까운 보물상자를 찾는다.
    for cx, cy in treasure_boxs:
        distance = math.sqrt((cx - x) * (cx - x) + (cy - y) * (cy - y))

        if smallest_distance > distance:
            smallest_distance = distance

    smallest_distance = round(smallest_distance)

    if smallest_distance == 0:
        treasure_boxs.remove([x, y])
        return '가라앉은 보물상자를 찾았습니다!'
    elif smallest_distance >= 10:
        board[x][y] = 'X'
        return '음파탐지기는 아무것도 탐지하지 못했습니다. 보물상자가 근처에 없습니다.'
    else:
        board[x][y] = f'{smallest_distance}'
        return f'음파탐지기에서 {smallest_distance} 떨어진 곳에 보물이 탐지되었습니다.'


def enter_player_move(previous_moves):
    print('다음 음파탐지기를 어디에 떨어뜨리겠습니까? (0-59 0-14) (또는 quit)')
    while True:
        move = input()
        if move.lower() == 'quit':
            print('게임 이용에 감사합니다!')
            sys.exit()

        move = move.split()
        if len(move) != 2 or move[0].isdigit() is False or move[1].isdigit() is False or \
                is_on_board(int(move[0]), int(move[1])) is False:
            print('0-59까지의 숫자를 입력하고 공백을 입력한 다음 0-14까지의 숫자를 입력하세요!')
        elif move in previous_moves:
            print('이전에 떨어뜨린 적이 있는 좌표입니다. 다시 입력하세요!')
        else:
            return list(map(int, move))


def main():
    print('S O N A R !')
    print()
    print('음파탐지기를 떨어뜨려서 가라앉은 보물상자를 찾아보세요!')

    while True:
        sonar_device_count = 20
        the_board = init_board()
        treasure_boxs = get_treasure_boxs(3)
        draw_board(the_board)
        previous_moves = []

        while sonar_device_count > 0:
            print(f'음파탐지기가 {sonar_device_count}개 남았습니다. 보물상자는 {len(treasure_boxs)}개 남았습니다.')

            x, y = enter_player_move(previous_moves)
            previous_moves.append([x, y])

            move_result = make_moves(the_board, treasure_boxs, x, y)
            if move_result == '가라앉은 보물상자를 찾았습니다!':
                for x, y in previous_moves:
                    make_moves(the_board, treasure_boxs, x, y)

            draw_board(the_board)
            print(move_result)

            if len(treasure_boxs) == 0:
                print('가라앉은 보물상자를 모두 찾았습니다. 축하합니다!')
                break

            sonar_device_count -= 1

        if sonar_device_count == 0:
            print('보물 찾기가 실패하였습니다.')

        print('게임을 다시 시작하시겠습니까? (yes or no)', end='')
        if input().lower().startswith('y') is False:
            break


if __name__ == '__main__':
    main()

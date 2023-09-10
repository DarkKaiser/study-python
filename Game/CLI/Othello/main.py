import copy
import random
import sys


def get_new_board():
    board = []
    for x in range(8):
        board.append([' '] * 8)

    return board


def reset_board(board):
    for x in range(8):
        for y in range(8):
            board[x][y] = ' '

    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'


def draw_board(board):
    HLINE = '  +---+---+---+---+---+---+---+---+'

    print('    1   2   3   4   5   6   7   8')
    print(HLINE)
    for y in range(8):
        print(f'{y + 1} |', end=' ')
        for x in range(8):
            print(f'{board[x][y]} |', end=' ')
        print()
        print(HLINE)


def get_score_of_board(board):
    x_score = 0
    o_score = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                x_score += 1
            elif board[x][y] == 'O':
                o_score += 1

    return {'X': x_score, 'O': o_score}


def is_on_board(x, y):
    return 0 <= x <= 7 and 0 <= y <= 7


def make_move(board, tile, x_start, y_start):
    tiles_to_flip = is_valid_move(board, tile, x_start, y_start)
    if tiles_to_flip is False:
        return False

    board[x_start][y_start] = tile
    for x, y in tiles_to_flip:
        board[x][y] = tile

    return True


def get_board_copy(board):
    return copy.deepcopy(board)


def is_on_corner(x, y):
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 7 and y == 7) or (x == 0 and y == 7)


def is_valid_move(board, tile, x_start, y_start):
    if board[x_start][y_start] != ' ' or is_on_board(x_start, y_start) is False:
        return False

    board[x_start][y_start] = tile

    if tile == 'X':
        other_tile = 'O'
    else:
        other_tile = 'X'

    tiles_to_flip = []
    for x_direction, y_direction in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = x_start, y_start
        x += x_direction
        y += y_direction
        if is_on_board(x, y) is True and board[x][y] == other_tile:
            while board[x][y] == other_tile:
                x += x_direction
                y += y_direction
                if is_on_board(x, y) is False:
                    break

            if is_on_board(x, y) is False:
                continue

            if board[x][y] == tile:
                while True:
                    x -= x_direction
                    y -= y_direction
                    if x == x_start and y == y_start:
                        break

                    tiles_to_flip.append([x, y])

    board[x_start][y_start] = ' '
    if len(tiles_to_flip) == 0:
        return False

    return tiles_to_flip


def get_board_with_hints(board, tile):
    copied_board = get_board_copy(board)
    for x, y in get_valid_moves(copied_board, tile):
        copied_board[x][y] = '.'

    return copied_board


def get_valid_moves(board, tile):
    valid_moves = []
    for x in range(8):
        for y in range(8):
            if is_valid_move(board, tile, x, y) is not False:
                valid_moves.append([x, y])

    return valid_moves


def enter_player_tile():
    while True:
        print(f'두 개의 타일(X 또는 O) 중에서 하나를 선택하세요:', end='')
        tile = input().upper()
        if tile in ['X', 'O']:
            if tile == 'X':
                return ['X', 'O']
            else:
                return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        print('컴퓨터부터 게임을 시작합니다.')
        return 'computer'
    else:
        print('플레이어부터 게임을 시작합니다.')
        return 'player'


def get_computer_move(board, computer_tile):
    possible_moves = get_valid_moves(board, computer_tile)

    for x, y in possible_moves:
        if is_on_corner(x, y) is True:
            return [x, y]

    random.shuffle(possible_moves)

    best_move = None
    best_score = -1
    for x, y in possible_moves:
        copied_board = get_board_copy(board)
        make_move(copied_board, computer_tile, x, y)
        score = get_score_of_board(copied_board)[computer_tile]
        if score > best_score:
            best_score = score
            best_move = [x, y]

    return best_move


def get_player_move(board, player_tile):
    digits_1_to_8 = '1 2 3 4 5 6 7 8'.split()

    while True:
        print('이동할 좌표를 입력하시거나, \'quit\'를 입력하여 게임을 종료하거나, \'hints\'를 켜거나 끕니다.')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'

        if len(move) == 2 and move[0] in digits_1_to_8 and move[1] in digits_1_to_8:
            x = int(move[0]) - 1
            y = int(move[1]) - 1
            if is_valid_move(board, player_tile, x, y) is False:
                continue
            else:
                break
        else:
            print('유효한 움직임이 아닙니다. X좌표(1-8)를 입력한 다음 Y좌표(1-8)를 입력하세요.')
            print('예를들어, 81은 오른쪽 상단 모서리입니다.')

    return [x, y]


def show_points(board, player_tile, computer_tile):
    scores = get_score_of_board(board)
    print(f'플레이어:{scores[player_tile]}점, 컴퓨터:{scores[computer_tile]}점')


def play_again():
    print('게임을 다시 시작하시겠습니까? (yes or no):', end='')
    return input().lower().startswith('y')


def main():
    print('오델로 게임에 오신것을 환영합니다!')

    while True:
        main_board = get_new_board()
        reset_board(main_board)
        player_tile, computer_tile = enter_player_tile()
        show_hints = False
        turn = who_goes_first()

        while True:
            if turn == 'player':
                if show_hints is True:
                    draw_board(get_board_with_hints(main_board, player_tile))
                else:
                    draw_board(main_board)

                show_points(main_board, player_tile, computer_tile)
                move = get_player_move(main_board, player_tile)
                if move == 'quit':
                    print('게임을 플레이 해 주셔서 감사합니다!')
                    sys.exit()
                elif move == 'hints':
                    show_hints = not show_hints
                    continue
                else:
                    make_move(main_board, player_tile, move[0], move[1])

                if get_valid_moves(main_board, computer_tile) == []:
                    break
                else:
                    turn = 'computer'
            else:
                draw_board(main_board)
                show_points(main_board, player_tile, computer_tile)
                input('컴퓨터의 움직임을 보려면 Enter 키를 누르세요.')
                x, y = get_computer_move(main_board, computer_tile)
                make_move(main_board, computer_tile, x, y)

                if get_valid_moves(main_board, player_tile) == []:
                    break
                else:
                    turn = 'player'

        draw_board(main_board)
        scores = get_score_of_board(main_board)
        print(f'O:{scores["O"]}점, X:{scores["X"]}점')
        if scores[player_tile] > scores[computer_tile]:
            print(f'컴퓨터를 {scores[player_tile] - scores[computer_tile]}점 차이로 이겼습니다! 축하합니다!')
        elif scores[player_tile] < scores[computer_tile]:
            print(f'당신이 졌습니다. 컴퓨터가 당신을 {scores[computer_tile] - scores[player_tile]}점 차이로 이겼습니다!')
        else:
            print('게임을 비겼습니다.')

        if play_again() is False:
            break


if __name__ == '__main__':
    main()

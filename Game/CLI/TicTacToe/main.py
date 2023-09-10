import random


def draw_board(ttt_board):
    print()
    print(f' {ttt_board[7]} | {ttt_board[8]} | {ttt_board[9]} ')
    print(f'-----------')
    print(f' {ttt_board[4]} | {ttt_board[5]} | {ttt_board[6]} ')
    print(f'-----------')
    print(f' {ttt_board[1]} | {ttt_board[2]} | {ttt_board[3]} ')
    print()


def input_player_letter():
    while True:
        print('사용하실 문자(\'O\' 또는 \'X\')를 입력하세요!:', end=' ')

        letter = input().upper()
        if letter == 'O':
            return ['O', 'X']
        elif letter == 'X':
            return ['X', 'O']

        print('입력을 잘못하셨습니다.')


def who_starts_first():
    return random.choice(['컴퓨터', '플레이어'])


def is_space_free(ttt_board, move):
    return ttt_board[move] == ' '


def get_player_move(ttt_board):
    move = ' '
    while move not in '123456789' or is_space_free(ttt_board, int(move)) is False:
        print('어디에 놓으시겠습니까?(1-9):', end=' ')
        move = input()

    return int(move)


def is_winner(ttt_board, letter):
    return ((ttt_board[1] == letter and ttt_board[2] == letter and ttt_board[3] == letter) or
            (ttt_board[4] == letter and ttt_board[5] == letter and ttt_board[6] == letter) or
            (ttt_board[7] == letter and ttt_board[8] == letter and ttt_board[9] == letter) or
            (ttt_board[1] == letter and ttt_board[4] == letter and ttt_board[7] == letter) or
            (ttt_board[2] == letter and ttt_board[5] == letter and ttt_board[8] == letter) or
            (ttt_board[3] == letter and ttt_board[6] == letter and ttt_board[9] == letter) or
            (ttt_board[3] == letter and ttt_board[5] == letter and ttt_board[7] == letter) or
            (ttt_board[1] == letter and ttt_board[5] == letter and ttt_board[9] == letter))


def get_computer_move(ttt_board, computer_letter, player_letter):
    # 한번만 두면 이길수 있는 곳이 있는지 확인한다.
    for i in range(1, len(ttt_board)):
        if is_space_free(ttt_board, i) is True:
            copy_board = ttt_board.copy()
            copy_board[i] = computer_letter
            if is_winner(copy_board, computer_letter) is True:
                return i

    # 한번만 두면 플레이어가 이길수 있는 곳이 있는지 확인한다.
    for i in range(1, len(ttt_board)):
        if is_space_free(ttt_board, i) is True:
            copy_board = ttt_board.copy()
            copy_board[i] = player_letter
            if is_winner(copy_board, player_letter) is True:
                return i

    # 코너가 비어있는지 확인한다.
    possible_moves = []
    for i in [1, 3, 7, 9]:
        if is_space_free(ttt_board, i) is True:
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)

    # 중앙이 비어있는지 확인한다.
    if is_space_free(ttt_board, 5) is True:
        return 5

    # 남은 영역 중에서 한 군데를 선택한다.
    possible_moves = []
    for i in [2, 4, 6, 8]:
        if is_space_free(ttt_board, i) is True:
            possible_moves.append(i)

    if len(possible_moves) != 0:
        return random.choice(possible_moves)

    return None


def is_board_full(ttt_board):
    for i in range(1, len(ttt_board)):
        if is_space_free(ttt_board, i) is True:
            return False

    return True


def play_again():
    print('게임을 다시 시작하시겠습니까? (yes or no)', end=' ')
    return input().lower().startswith('y')


def main():
    print('틱택토 게임에 오신것을 환영합니다!')

    while True:
        ttt_board = [' '] * 10
        player_letter, computer_letter = input_player_letter()
        print()

        turn = who_starts_first()
        print(f'{turn}부터 게임을 시작합니다.')

        while True:
            if turn == '컴퓨터':
                move = get_computer_move(ttt_board, computer_letter, player_letter)
                ttt_board[move] = computer_letter

                if is_winner(ttt_board, computer_letter) is True:
                    draw_board(ttt_board)
                    print('컴퓨터가 이겼습니다. 당신이 패배하였습니다!')
                    break
                else:
                    turn = '플레이어'
            else:
                draw_board(ttt_board)

                move = get_player_move(ttt_board)
                ttt_board[move] = player_letter

                if is_winner(ttt_board, player_letter) is True:
                    draw_board(ttt_board)
                    print('축하합니다. 당신이 게임에서 이겼습니다.')
                    break
                else:
                    turn = '컴퓨터'

            # 무승부인지 확인한다.
            if is_board_full(ttt_board) is True:
                draw_board(ttt_board)
                print('무승부입니다.')
                break

        if play_again() is False:
            break


if __name__ == '__main__':
    main()

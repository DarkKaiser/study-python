import random

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole monkey moose mouse mule newt otter owl panda parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf wombat zebra'.split()


def get_random_word(word_list):
    return word_list[random.randint(0, len(word_list) - 1)]


def display_board(missed_letters, correct_letters, secret_word):
    print(HANGMANPICS[len(missed_letters)])
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        letter = secret_word[i]
        if letter in correct_letters:
            blanks = blanks[:i] + letter + blanks[i + 1:]

    print('* 시크릿 단어:', end=' ')
    for letter in blanks:
        print(letter, end=' ')
    print()

    print('* 추측 실패 문자:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()


def get_guess(already_guessed):
    while True:
        print('* 새 추측 문자를 입력하세요:', end=' ')

        guess = input().lower()
        if len(guess) != 1:
            print('  > 한 문자만 입력 가능합니다.')
        elif guess in already_guessed:
            print('  > 이전에 입력하셨던 문자입니다.')
        elif guess.isalpha() is False:
            print('  > 알파벳만 입력 가능합니다.')
        else:
            return guess


def play_again():
    print("다시 플레이 하시겠습니까? (yes or no)", end=' ')
    return input().lower().startswith('y')


def main():
    print('H A N G M A N')

    missed_letters = ''
    correct_letters = ''
    secret_word = get_random_word(words)
    game_is_done = False

    while True:
        display_board(missed_letters, correct_letters, secret_word)

        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters += guess

            found_all_letters = True
            for letter in secret_word:
                if letter not in correct_letters:
                    found_all_letters = False
                    break

            if found_all_letters is True:
                print(f'정답입니다! 시크릿 단어는 \'{secret_word}\'이였습니다! 당신이 이겼습니다!')
                game_is_done = True
        else:
            missed_letters += guess

            if len(missed_letters) == (len(HANGMANPICS) - 1):
                display_board(missed_letters, correct_letters, secret_word)
                print(
                    f'실패하였습니다!\n추측 실패 문자는 \'{missed_letters}\', 추측 성공 문자는 \'{correct_letters}\', 시크릿 단어는 \'{secret_word}\'이었습니다!')
                game_is_done = True

        if game_is_done is True:
            if play_again() is True:
                missed_letters = ''
                correct_letters = ''
                secret_word = get_random_word(words)
                game_is_done = False
            else:
                break


if __name__ == '__main__':
    main()

import os

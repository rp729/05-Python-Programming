import random

'''Global vars'''
file = open('words.txt')
game_dic = {}

def main():
    play_game = game()
    return play_game

'''Main function'''
def game():
    attempt = 6
    attempt_list = []
    word = word_generator()
    word_count = len(word)
    board = game_board(word)
    game_mode = mode()
    '''word_count will hit 0 when the user wins'''
    while attempt > 0 and word_count > 0:
        ascii_gui(attempt)
        pretty_board = ''.join(board)
        print(pretty_board,f'\nYou have {attempt} attempts left!'\
                           f'\nAttempts made:{attempt_list}')
        if game_mode == 1:
            print(easy(word,attempt_list))
        user_input = input("Enter a letter:").lower()
        user_input = input_validation(user_input,attempt_list)
        if user_input in word:
            '''Finds all indexed occurances of user input with indices() function'''
            occurances = indices(word,user_input)
            for i in occurances:
                board.pop(i)
                board.insert(i,word[i])
            word_count -= word.count(user_input)
        else:
            attempt -= 1
        attempt_list.append(user_input)
    '''Function to find if user won or lost'''
    result = print(win_lose(word_count,word))
    ascii_gui(attempt)
    return result

'''This will create a library based on the given text file'''
def lib_create():
    count = 1
    for i in file:
        game_dic[count] = i.strip('\n')
        count += 1
    return count

'''This will format the gameboard'''
def game_board(word):
    result = []
    for i in range(len(word)):
        result.append('_ ')
    return result

'''Chosses a random word'''
def word_generator():
    count = lib_create()
    num = random.randint(1, count)
    return game_dic[num]

'''Simple input validation'''
def input_validation(self,list):
    while len(self) != 1 or str.isalpha(self) == False or self in list:
        self = input(f'INVALID INPUT: Enter a letter:')
    return self

'''Finds all occurances of a character'''
def indices(word,guess):
    occurances = []
    for i in range(len(word)):
        if guess == word[i]:
            occurances.append(i)
        else:
            continue
    return occurances

'''Function to find if user won or lost'''
def win_lose(win,word):
    if win == 0:
        return f'CONGRATS! YOU WIN! the word was {word}'
    else:
        return f'LOSER! The word was {word}'

'''ASCII ART'''
def ascii_gui(attempt):
    file = open(f'hangman_{attempt}.txt')
    read = file.read()
    print(read)
    file.close()
    return

'''Choose easy or hard mode with input validation'''
def mode():
    mode_choice = input("Choose your game below:"\
                        "\n(Easy mode utilizes advanced algorithms to reccomend possible letters for the word provided)"
                        "\n1) EASY MODE"\
                        "\n2) HARD MODE"\
                        "\nRESPONSE:").lower()
    solutions = ['1','2','easy','easy mode','hard','hard mode']
    while mode_choice not in solutions:
        print("INVALID INPUT!")
        mode_choice = input("Choose your game below:" \
                            "\n(Easy mode utilizes advanced algorithms to reccomend possible letters for the word provided)"
                            "\n1) EASY MODE" \
                            "\n2) HARD MODE" \
                            "\nRESPONSE:").lower()
    if mode_choice == '1' or mode_choice == 'easy' or mode_choice == 'easy mode':
        print("You selected: EASY MODE")
        return 1
    else:
        print("You selected: HARD MODE")
        return 2

'''Generates letters to reccomend'''
def easy(word,user_list):
    letters = list('abcdefghijklmnopqrstuvwxyz')
    word = list(word)
    word_list = []
    while len(word_list) < 4:
        correct_letter = word[random.randint(0,len(word)-1)].lower()
        random_letter = letters[random.randint(0,len(letters)-1)].lower()
        if correct_letter in user_list:
            continue
        elif random_letter in user_list or random_letter in word_list:
            continue
        else:
            word_list.append(correct_letter)
            word_list.append(random_letter)
    new_list = set(word_list)
    return f'Reccomended letters: {", ".join(list(new_list)).upper()}'


main()

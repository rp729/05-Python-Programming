import random

'''Global vars'''
file = open('words.txt')
game_dic = {}

'''Main function'''
def main():
    attempt = 6
    attempt_list = []
    word = word_generator()
    word_count = len(word)
    board = game_board(word)
    '''word_count will hit 0 when the user wins'''
    while attempt > 0 and word_count > 0:
        ascii_gui(attempt)
        pretty_board = ''.join(board)
        print(pretty_board,f'\nAttempts made:{attempt_list}'\
              f'\nYou have {attempt} attempts left!')
        user_input = input("Enter a letter:").lower()
        user_input = input_validation(user_input,attempt_list)
        if user_input in word:
            '''Finds all indexed occurances of user input with indices() function'''
            occurances = indices(word,user_input)
            for i in occurances:
                board.pop(i)
                board.insert(i,word[i])
            word_count -= 1
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
        self = input(f'INVALID INPUT: Enter only one letter:')
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

main()
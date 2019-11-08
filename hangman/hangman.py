import random

'''Global vars'''
file = open('words.txt')
game_dic = {}

'''Main function'''
def main():
    attempt = 7
    attempt_list = []
    '''Generate a word from function created'''
    word = word_generator()
    '''Build a gameboard from function created'''
    board = game_board(word)
    '''This is where the game begins'''
    word_count = len(word)
    while attempt > 0 and word_count > 0:
        '''Print out the board or number of attempts along with attempts made'''
        pretty_board = ''.join(board)
        print(pretty_board,f'\nAttempts made:{attempt_list}')
        print(f'You have {attempt} attempts left!')
        user_input = input("Enter a letter:")
        '''Run user input through input validation on function created'''
        user_input = input_validation(user_input,attempt_list)
        if user_input in word:
            '''Finds all indexed occurances of user input with indices() function'''
            occurances = indices(word,user_input)
            for i in occurances:
                board.pop(i)
                board.insert(i,word[i])
        else:
            attempt -= 1
        attempt_list.append(user_input)
    if word_count == 0:
        print("CONGRATS! YOU WIN!")
    else:
        print(f'LOSER! The word was {word}')
    return

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

main()
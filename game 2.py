max_attemots = 5
import random
WORD_LIST= ['name', 'car', 'plane', 'dog', 'stuff']
def pick_word(listword):
    word = random.choice(listword)
    print('the word is:', word)
    return word
def get_guess():
    print('running get guess')
    guess= input('guess a word:')
    if not guess =='':
             return guess
    else:
        print('words cannot be empty')

get_guess()

def evaluate_guess(attempts_list):
        word= pick_word(WORD_LIST)
        if attempts_left == max_attempts:
            word = word
        else:
            word = pick_word(WORD_LIST)
        if guess == word:
            return True
            print('your guess is correct')
        else:
            return False
            print('try again')
            
def play_game():
    if evaluate_guess() == True:
        print('your answer is correct')
        resp =input('do you want to continue Y/N')
        if resp == 'Y':
            play_game()
        else:
            print('goodbye')

play_game()

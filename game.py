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
def evaluate_guess():
    print('running evaluate guess')
    word = pick_word(WORD_LIST)
    guess = get_guess()
    if guess== word:
        return True

    else:
        return False
            
def play_game():
    if evaluate_guess() == True:
        print('your answer is correct')
        resp =input('do you want to continue Y/N')
        if resp == 'Y':
            play_game()
        else:
            print('goodbye')

play_game()


max_attempts = 5
WORD_LIST =['name','car','plane','team','stuff','crap']
import random

def pick_word(list_word):
    word = random.choice(list_word)
    return word
def get_guess():
    print('running get_guess')
    guess= input('guess a word:')
    if not guess == '':
          return guess
    else:
          print('words cannot be empty')
          get_guess()
##def evaluate_guess(attempts_left):
##    guess = get_guess()
##    word= ''
##    if  attempts_left ==5:
##        word= pick_word(WORD_LIST)
##        if guess == word:
##            print('your word is correct')
##            retry= input('do you want to try again? Y/N')
##        if  retry = 'Y':
##            word = pick_word(WORD_LIST)
##            attempts_left -=1
##        else:
##            attempts_left -=1
##            print('wrong guess')
##            guess= get_guess()
##            evaluate_guess(attempts_left)
##
##
##
##def play_game():
##    while True:
##        game_count +=1
##        attempts =0
##        word = pick_word(WORD_LIST)
##        guess = get_guess()
##        evaluate_guess(guess,word,attempts)
##        


def evaluate_guess(word,attempts):
    print(word)
    while attempts >0:
        guess = get_guess()
        if guess != word:
            attempts -=1
            print('wrong attempts,you have', attempts, 'attempts left')
            evaluate_guess(word,attempts)
        else:
            print('your guess is correct')
            return True
        break

        

    else:
            print('you have used up your attempts')
            return False

            



def play_game(game_count):
    game_count += 1
    word = pick_word(WORD_LIST)
    print('Welcome to word guess game')
    print()
    while evaluate_guess(word,5):
        ask = input('do you want to continue? Y/N')
        if ask == 'Y':
            play_game(game_count)
        else:
            print('you played',game_count,'games')
            print('goodbye')
            exit()

    else:
            print('oops you missed that one')
            retry = input('do you want to try another word?')
            if retry == 'Y':
                play_game(game_count)
            else:
                print('goodbye')

play_game(0)
            
        
    

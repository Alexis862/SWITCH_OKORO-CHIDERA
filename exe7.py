WORD='elephant'
def displayBoard(missedLetters, correctLetters, WORD):
    print([len(missedLetters)])
    print()

    print('Missed letters', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(WORD)
    for i in range(len(WORD)):
        if WORD[i] in correctLetters:
            blanks = blanks[:i] + WORD[i] + blanks[i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()
def getGuess(alreadyGuessed):
    while True:
        print('guess a letter:')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('please enter a single letter.')
        elif guess in alreadyGuessed:
            print('you have guessed this letter. Choose again')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('please enter a letter')
        else:
            return guess

def play_again():
    print('Do you want to play again? y/n')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
WORD=''
game_Is_Done = False

while True:
    displayBoard(missedLetters, correctLetters, WORD)
    guess = getGuess(missedLetters + correctLetters)

    if guess in WORD:
        correctLetters = correctLetters + guess

        found_all_letters = True
        for i in range(len(WORD)):
            if WORD[i] not in correctLetters:
                found_all_letters = False
                break
        if found_all_letters:
            print('HUURRAYYY!!!!!, YOU HAVE FOUND ',WORD, 'YOU WON')
            game_Is_Done = True
        else:
            missedLetters = missedLetters + guess

        if game_Is_Done:
                if playAgain():
                  missedLetters = ''
                  correctLetters = ''
                  game_is_done = False
                  WORD()
                else:
                  break
                  
                  
                                      



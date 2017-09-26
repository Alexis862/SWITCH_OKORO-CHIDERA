# program for the guess game of a number
print('====THE GUESS GAME====')
print('RULES:')
print('You have to guess a number between 1 and 10') 
print('You have ten attempts')
for i in range(10):
    from random import randint
    x = randint(1,10)
    if x==(eval(input('guess a word:'))):
        print('sucess')
        print('The answer is:', x)

    else:
        print('retry')
        print('The answer is:', x)

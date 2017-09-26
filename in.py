# program to find out if the letter a is in your string
s= input('enter a string:')
for i in range(len(s)):
    if s[i]=='a':
        print(i)
    else:
        print('the letter a is not in your string')

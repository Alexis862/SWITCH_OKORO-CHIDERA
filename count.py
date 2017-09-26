# program to find out if a number is prime or not
num = eval(input('enter a number'))

flag = 0
for i in range(2,num):
    if num%i==0:
        flag = 1
if flag==1:
    print('not prime')
else:
    print('prime')
                  

# program that prints the sum of the divisors of a number
s = 0
x= eval(input('enter a number:'))
for i in range(1,x+1):
    if x%i==0:
        print(i)
        s= s+i
print('the sum of the divisors of the number are', s)         
         

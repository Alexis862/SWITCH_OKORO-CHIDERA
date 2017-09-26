# a program that computes[1+(1/2)+(1/3)+....(1/n)]- In(n)
s = 0
from math import log
x = eval(input('enter a number:'))
for i in range(2,x+1):
         s = s + 1+(1/(i+1))
print(s-log(x))



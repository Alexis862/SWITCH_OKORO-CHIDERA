# program to convert celcius to fahrenheit and vice-versa
temp =eval(input('Write a temperature:'))
temp2 =input('state the unit c/f:')
f= ('f')
c= ('c')
celcius= 5/9*(temp-32)
fahrenheit= (9/5)*temp + 32

if f==temp2:
    print('this has been converted from',temp, 'fahrenheit to', celcius, 'celcius')

else:
    print('this has been converted from', temp, 'celcius to', fahrenheit, 'fahrenheit')

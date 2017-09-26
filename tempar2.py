temp= eval(input('enter a temperature in celcius:'))
if temp < -273.15:
    print('invalid vecause it is below absolute zero')
if temp == -273.15:
    print('temperature is absolute zero')
if temp >-273.15 and temp <0:
    print('temperature is below freezing')
if temp == 0:
    print('the temperature is at freezing point')
if temp  >0 and temp <100:
    print('the temperature is in normal range')
if temp == 100:
    print('the temperature is at boiling point')
if temp > 100:
    print('the temperature is above boiling point')

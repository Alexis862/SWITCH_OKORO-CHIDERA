# to count how many of the squares from 1 to 100 end in a 4 and how many end in a9
count = 0
for i in range(1,101):
    if (i**2)%10==4:
        count= count+1
print('there are', count, 'numbers from the squares of 1-100 that end in 4')
for i in range(1,101):
    if (i**2)%10==9:
        count= count+1
print('there are', count, 'numbers from the squares of 1-100 that end in 9')        

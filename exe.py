# to count how many of the squares from 1-100 end in 1
count = 0
for i in range(1,101):
    if (i**2)%10==1:
        count= count+1

print('there are',count,' numbers that end in 1 from the squares of 1-100')

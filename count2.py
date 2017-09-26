count = 0
for i in range(10000):
    from random import randint
    x = randint(1,100)
    if x%12==0:
        count= count+1
print(x)
print(count)

# program to compute the sum 1-2+3-4+...+1999-2000
s= 0
for i in range(1,2000,2):
    s= s+i
for i in range(2,2001,2):
    s= s-i    
print(s)

  


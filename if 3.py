# program to find out if a student is a freshman or a sophmore based on his/her credit
cred= eval(input('how many credits have you taken:'))
for i in range(54,84):
    if cred<= 23:
        print('this student is a freshman')
for x in range(84,100):
    if cred >24 and cred <53:
        print('this student is a sophomore')
    

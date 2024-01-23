def setbits(x,pos,num,y):
    part = y[len(y)-num:]
    d = x[:len(x)-pos] + part + x[len(x)-pos+len(part):]
    print('Hence the Modified X is : ',d)

num = int(input('\nEnter the Value of n : '))
pos = int(input('\nEnter the Value of Position : '))
x = input('\nEnter the First Binary Number : ')
y = input('\nEnter the Second Binary Number : ')
setbits(x,pos,num,y)

import random
num = int(input('\nEnter the value of N so that N random numbers in the range 0.0 - 1.0 to be Generated : '))
numbers1 = []
for i in range(num):
    numbers1.append(random.random())
numbers1.sort()
print('\nThe Randomly Generated Sequence from 0.0 - 1.0 containing ',num,' terms is : ',numbers1)
n = float(input('\nEnter the Upper Bound of the Sequence : '))
numbers2 = []
for i in range(num):
    numbers2.append(random.uniform(0.0,n))
numbers2.sort()
print('\nThe Randomly Generated Sequence from 0.0 - ',n,' containing ',num,' terms is : ',numbers2)

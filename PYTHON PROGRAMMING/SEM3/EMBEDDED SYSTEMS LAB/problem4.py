num = int(input('\nEnter the Negative Decimal Number : '))

s = bin(-num)[2:]
s = '1'+s

print('The Signed Magnitude of ',num,' : ',s)

one = ''
o = bin(-num)[2:]
for i in o:
    if i=='0':
        one+='1'
    else:
        one+='0'
if len(one)<=8:
    c = len(one)
    one = '1'*(8-len(one))+one
print('\nThe One\'s Complement of ',num,' : ',one)

two = one
two = bin(int(two,2)+int('1',2))[2:]
print('\nThe Two\'s Complement of ',num,' : ',two)

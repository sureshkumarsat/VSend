binary1 = input('\nEnter the First 8 bit Binary Number : ')
binary2 = input('\nEnter the Second 8 bit Binary Number : ')
nega = ''
for i in binary1:
    if i=='1':
        nega+='0'
    else:
        nega+='1'
negbinary1 = bin(int(nega,2)+int('1',2))
if len(negbinary1)>8:
    len1 = len(negbinary1)
    negbinary1 = negbinary1[len1-8+1:]
negb = ''
for i in binary2:
    if i=='1':
        negb+='0'
    else:
        negb+='1'
negbinary2 = bin(int(negb,2)+int('1',2))
if len(negbinary2)>8:
    len2 = len(negbinary2)
    negbinary2 = negbinary2[len2-8+1:]

bin1addbin2 = bin(int(binary1,2)+int(binary2,2))
bin1addnegbin2 = bin(int(binary1,2)+int(negbinary2,2))
negbin1addbin2 = bin(int(negbinary1,2)+int(binary2,2))
negbin1addnegbin2 = bin(int(negbinary1,2)+int(negbinary2,2))
bin1subbin2 = bin(int(binary1,2)-int(binary2,2))
bin1subnegbin2 = bin(int(binary1,2)-int(negbinary2,2))
negbin1subbin2 = bin(int(negbinary1,2)-int(binary2,2))
negbin1subnegbin2 = bin(int(negbinary1,2)-int(negbinary2,2))
print(bin1addbin2)
print(bin1addnegbin2)
print(negbin1addbin2)
print(negbin1addnegbin2)
print(bin1subbin2)
print(bin1subnegbin2)
print(negbin1subbin2)
print(negbin1subnegbin2)

import math
def pollard(n):
    a = 2
    i = 2
    while(True):
        print("a: ",a)
        print("i: ",i)
        a = (a**i) % n
        print("\n'a' value after taking power: ",a)
        d = math.gcd((a-1), n)
        print("gcd of",a-1,"&",n,": ",d)
        print("----------------------------------------")
        if (d > 1):
            return d
            break
        else:
            i += 1
  

num = int(input("Number: "))
n=num
ans = []
while(True):
   

    d = pollard(num)
    ans.append(d)
    r = int(num/d)
    c=0
    for i in range(1,int(r/2)):
        if r%i==0:
            c+=1
    if c>1:
        num = r
    else:
        ans.append(r)
        break
        
  
print("Prime factors of", n, "are", *ans)

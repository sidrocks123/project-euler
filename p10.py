import math as m

def primeCheck(n):
    i = 2
    flag = True
    while(i <= m.sqrt(n)):
        if(n % i == 0):
            flag = False
            break
        else:
            i = i + 1
    return flag

def primesLessThan(n):
    ans = []
    for temp in range(2,n):
        if(primeCheck(temp) == True):
            ans.append(temp)
    return ans

print(sum(primesLessThan(2000000)))
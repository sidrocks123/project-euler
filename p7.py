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

def firstNPrimes(n):
    ans = []
    count = 0
    temp = 2
    while(count != n):
        if(primeCheck(temp) == True):
            ans.append(temp)
            temp = temp + 1
            count = count + 1
        else:
            temp = temp + 1
    return ans

print((firstNPrimes(10001))[10000])
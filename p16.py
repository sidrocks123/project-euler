import math as m

def sumOfDigits(base, exp):
    # for exact form, not scientific notation
    n = int(m.pow(base,exp))
    temp = str(n)
    var = [int(i) for i in temp]
    ans = sum(var)
    return ans

print(sumOfDigits(2,1000))
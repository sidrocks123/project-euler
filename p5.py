def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    return (a / gcd(a,b)) * b

def lcmlist(inst):
    ans = 1
    for i in range(len(inst)):
        ans = lcm(ans,inst[i])
    return ans

print(lcmlist([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
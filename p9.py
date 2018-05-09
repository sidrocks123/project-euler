import math as m

def pyTripletWithSum(s):
    for a in range(1,1000):
        for b in range(1,1000):
            c = 1000 - (a+b)
            if(a*a + b*b == c*c):
                return a*b*c
                break

print(pyTripletWithSum(1000))
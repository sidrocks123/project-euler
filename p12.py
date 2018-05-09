def noOfDivisors(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    ans = [0] * len(primes)
    i = 0
    for prime in primes:
        while(n % prime == 0):
            ans[i] = ans[i] + 1
            n = n / prime
        i = i + 1 
    prod = 1
    for i in ans:
        if i != 0:
            prod = prod * (i+1)
    return prod

def triangularNumberWith500Divisors():
    num = 0
    for i in range(1, 20000):
        num = int(i * ((i+1)/2))
        if noOfDivisors(num) > 500:
            return num, i
            break

print(triangularNumberWith500Divisors())

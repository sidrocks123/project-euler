def sumOfIndSquares(n):
    ans = 0
    for i in range(1, n+1):
        ans = ans + (i*i)
    return ans

def sumOfBrackSquares(n):
    ans = 0
    for i in range(1, n+1):
        ans = ans + i
    return (ans * ans)

print(sumOfBrackSquares(100) - sumOfIndSquares(100))
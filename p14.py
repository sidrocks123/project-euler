def collatzSeq(n):
    count = 1
    while(n != 1):
        if(n%2 == 0):
            n = n / 2
        else:
            n = (3*n) + 1
        count = count + 1
    return count

def collatzSeqForList(N):
    number = 1
    seqCount = 1
    for num in range(1,N):
        temp = collatzSeq(num)
        if (temp > seqCount):
            seqCount = temp
            number = num
    return number, seqCount

print(collatzSeqForList(1000000))
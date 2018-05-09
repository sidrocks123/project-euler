import math as m

prime = []
num = 600851475143
flag = 0

def notprime(n, flag):
	for i in range(2,int(m.sqrt(n))):
		if(n % i == 0):
			flag = 1
			break
	return flag, i

newflag, factor = notprime(num, flag)
print(newflag)
print(factor)
print(num / factor)

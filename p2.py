evenfiblist = [2]
fiblist = [1,2]

def fib(n):
	a = 1
	b = 2
	c = 3
	while(c < n):
		c = a + b
		a = b
		b = c
		fiblist.append(c)
		if((c < n) and (c%2 == 0)):
			evenfiblist.append(c)


fib(4000000)
print(fiblist)
print(evenfiblist)
print(sum(evenfiblist))

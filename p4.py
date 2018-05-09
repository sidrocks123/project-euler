import math as m

def reverseNumber(n):
	rev = 0
	t = n
	#no = int(m.log10(n)) + 1
	no = len(str(n))
	while(no != 0):
		digit = t % 10
		rev = rev + (m.pow(10, no-1) * digit)
		no = no - 1
		t = int(t / 10)
	return rev

def isPalindrome(n):
	rev = reverseNumber(n)
	if(n == rev):
		return True
	else:
		return False

def largestPalindrome():
	ans = 0
	anslist = []
	for i in range(999, 100, -1):
		for j in range(999, 100, -1):
			ans = i*j
			truth = isPalindrome(ans)
			if truth == True:
				anslist.append(ans)
	return anslist

#print(isPalindrome(723))
#print(isPalindrome(232))
print(max(largestPalindrome()))
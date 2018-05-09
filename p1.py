i = 3
j = 5
k = 15
sumof3 = 0
sumof5 = 0
sumof15 = 0

while(i < 1000):
	sumof3 = sumof3 + i
	i = i + 3

while(j < 1000):
	sumof5 = sumof5 + j
	j = j + 5

while(k < 1000):
	sumof15 = sumof15 + k
	k = k + 15

print(sumof3 + sumof5 - sumof15)
